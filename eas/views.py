from django.shortcuts import render
from .models import Soal, Santri, Nilai, Evaluasi
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import EvaluasiForm
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    context = {
        'santri': Santri.objects.get(user=request.user)
    }
    return render(request, 'index.html', context)

def evaluasi(request):
    santri = Santri.objects.get(user=request.user)

    soal_ids = request.session.get('soal_ids')
    if soal_ids:
        # ambil soal berdasarkan ID yang disimpan di session
        soal_list = list(Soal.objects.filter(id__in=soal_ids))
    else:
        # pertama kali buka halaman → acak soal
        semua_soal = list(Soal.objects.all())
        soal_list = random.sample(semua_soal, 4) 
        # simpan ID soal di session supaya tidak berubah sampai submit
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

                # Simpan jawaban ke Evaluasi
                Evaluasi.objects.create(
                    santri=santri,
                    soal=soal,
                    jawaban_santri=jawaban_user,
                    is_correct=is_correct
                )

            # Hitung skor
            skor = (benar / len(soal_list)) * 100
            durasi = form.cleaned_data.get('durasi_detik') or 0

            # Simpan atau update Nilai
            Nilai.objects.update_or_create(
                santri=santri,
                defaults={'nilai_akhir': skor, 'durasi_detik': durasi}
            )

            # Hapus soal dari session setelah submit
            if 'soal_ids' in request.session:
                del request.session['soal_ids']

            # Redirect ke halaman peringkat
            return redirect('peringkat')

    else:
        # GET → buat form baru
        form = EvaluasiForm(soal_list=soal_list)

    return render(request, 'evaluasi.html', {'form': form})


def peringkat(request):
    peringkat_list = Nilai.objects.all().order_by('-nilai_akhir')
    context = {
        'peringkat': peringkat_list
    }
    return render(request, 'peringkat.html', context)
