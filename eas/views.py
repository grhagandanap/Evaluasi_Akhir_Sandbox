from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Soal, Santri, Nilai, Evaluasi
from .forms import EvaluasiForm
import random


def home(request):
    """
    View for the homepage.

    If the user is already authenticated, redirect them to the main dashboard (`index` view).
    Otherwise, render the homepage for unauthenticated visitors.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        - Redirects to the dashboard if logged in.
        - Renders 'home.html' template otherwise.
    """
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'home.html')


@login_required
def index(request):
    """
    Dashboard view for authenticated users.

    Displays the user's profile information and checks if the user
    has already completed the evaluation.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object from the logged-in user.

    Returns
    -------
    HttpResponse
        Renders 'index.html' template with:
        - `santri`: The Santri (student) object linked to the user.
        - `sudah_mengerjakan`: Boolean indicating if the user has taken the test.
    """
    santri = Santri.objects.get(user=request.user)
    sudah_mengerjakan = Nilai.objects.filter(santri=santri).exists()

    context = {
        'santri': santri,
        'sudah_mengerjakan': sudah_mengerjakan
    }
    return render(request, 'index.html', context)


@login_required
def evaluasi(request):
    """
    View for conducting the evaluation (quiz/exam).

    - Prevents users who have already completed the test from re-taking it.
    - Randomly selects a set of questions (4 by default) and stores them in the session.
    - On form submission, evaluates answers, records individual results, and stores the final score.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        - Renders 'evaluasi.html' with the evaluation form if GET request.
        - Redirects to 'peringkat' (ranking page) after successful submission.

    Notes
    -----
    - `EvaluasiForm` is dynamically built with question instances.
    - Session key `soal_ids` stores selected question IDs to ensure consistency during submission.
    """
    santri = Santri.objects.get(user=request.user)

    # Prevent re-evaluation
    if Nilai.objects.filter(santri=santri).exists():
        return redirect('index')

    # Retrieve or create a random set of questions
    soal_ids = request.session.get('soal_ids')
    if soal_ids:
        soal_list = list(Soal.objects.filter(id__in=soal_ids))
    else:
        semua_soal = list(Soal.objects.all())
        soal_list = random.sample(semua_soal, 4)
        request.session['soal_ids'] = [s.id for s in soal_list]

    if request.method == 'POST':
        form = EvaluasiForm(request.POST, soal_list=soal_list)
        if form.is_valid():
            benar = 0
            for soal in soal_list:
                jawaban_user = form.cleaned_data.get(f'jawaban_{soal.id}')
                jawaban_benar = soal.jawaban_benar
                is_correct = jawaban_user == jawaban_benar

                if is_correct:
                    benar += 1

                # Save detailed answer result
                Evaluasi.objects.create(
                    santri=santri,
                    soal=soal,
                    jawaban_santri=jawaban_user,
                    is_correct=is_correct
                )

            # Calculate score
            skor = (benar / len(soal_list)) * 100
            durasi = form.cleaned_data.get('durasi_detik') or 0

            # Save or update final score
            Nilai.objects.update_or_create(
                santri=santri,
                defaults={'nilai_akhir': skor, 'durasi_detik': durasi}
            )

            # Clear session data
            request.session.pop('soal_ids', None)

            return redirect('peringkat')
    else:
        form = EvaluasiForm(soal_list=soal_list)

    return render(request, 'evaluasi.html', {'form': form})


@login_required
def arsip(request):
    """
    View for displaying the user's evaluation archive.

    Shows all questions the user has answered, along with correctness information
    and the computed overall score.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request from the authenticated user.

    Returns
    -------
    HttpResponse
        Renders 'arsip.html' template with:
        - `arsip_list`: All question-answer records of the user.
        - `benar_count`: Total number of correct answers.
        - `total_soal`: Total number of answered questions.
        - `skor`: Computed overall score (integer percentage).
    """
    santri = Santri.objects.get(user=request.user)
    arsip_list = (
        Evaluasi.objects
        .filter(santri=santri)
        .select_related('soal')
        .prefetch_related('soal__pilihan')
    )

    benar_count = arsip_list.filter(is_correct=True).count()
    total_soal = arsip_list.count()
    skor = (benar_count / total_soal * 100) if total_soal > 0 else 0

    context = {
        'arsip_list': arsip_list,
        'benar_count': benar_count,
        'total_soal': total_soal,
        'skor': int(skor),
    }
    return render(request, 'arsip.html', context)


@login_required
def peringkat(request):
    """
    View for displaying the ranking leaderboard.

    Lists all participants (`Nilai` records) ordered by their final scores (`nilai_akhir`).

    Parameters
    ----------
    request : HttpRequest
        The HTTP request from the authenticated user.

    Returns
    -------
    HttpResponse
        Renders 'peringkat.html' template with:
        - `peringkat`: List of all users sorted by score (descending).
    """
    peringkat_list = Nilai.objects.all().order_by('-nilai_akhir')
    context = {'peringkat': peringkat_list}
    return render(request, 'peringkat.html', context)
