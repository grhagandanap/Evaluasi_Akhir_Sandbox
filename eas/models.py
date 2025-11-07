from django.db import models
from django.contrib.auth.models import User

# Choices for multiple-choice questions
GRADE_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class Santri(models.Model):
    """
    Model representing a student (evaluation participant).

    Each student is optionally linked to a Django `User` account through a
    one-to-one relationship and stores basic personal information such as
    name, age, address, and gender.

    Attributes
    ----------
    user : OneToOneField
        Optional relationship to the Django `User` model for authentication.
    nama : CharField
        The student's full name.
    santri_id : CharField
        A unique student ID, with the default format "ARX000-00000".
    usia : IntegerField
        The student's age in years.
    alamat : TextField
        The student's residential address.
    gender : CharField
        The student's gender ('I' for Ikhwan, 'A' for Akhwat).

    Methods
    -------
    __str__()
        Returns the student's name as the string representation.
    """
    GENDER_CHOICES = [
        ('I', 'Ikhwan'),
        ('A', 'Akhwat'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    nama = models.CharField(max_length=100)
    santri_id = models.CharField(
        max_length=12, unique=True, default="ARX000-00000"
    )
    usia = models.IntegerField()
    alamat = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.nama


class Soal(models.Model):
    """
    Model representing an evaluation question.

    Each `Soal` contains a question text and one correct answer
    selected from options A, B, C, or D.

    Attributes
    ----------
    teks_soal : TextField
        The text of the question.
    jawaban_benar : CharField
        The correct answer code (A/B/C/D) according to `GRADE_CHOICES`.

    Methods
    -------
    __str__()
        Returns the question text as the string representation.
    """
    teks_soal = models.TextField()
    jawaban_benar = models.CharField(max_length=1, choices=GRADE_CHOICES)

    def __str__(self):
        return self.teks_soal


class PilihanJawaban(models.Model):
    """
    Model representing answer choices for each question.

    Each answer choice is linked to a specific `Soal` through a foreign key
    relationship and contains both a choice code (A–D) and the answer text.

    Attributes
    ----------
    soal : ForeignKey
        The related `Soal` instance for this answer choice.
    kode_pilihan : CharField
        The letter representing the choice (A/B/C/D).
    teks_pilihan : CharField
        The textual content of the answer choice.

    Methods
    -------
    __str__()
        Returns a formatted string like "A. Answer Text".
    """
    soal = models.ForeignKey(
        Soal, on_delete=models.CASCADE, related_name='pilihan'
    )
    kode_pilihan = models.CharField(max_length=1, choices=GRADE_CHOICES)
    teks_pilihan = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.kode_pilihan}. {self.teks_pilihan}"


class Evaluasi(models.Model):
    """
    Model that stores the evaluation results (answers) for each student and question.

    Each record logs a student's answer to a specific question,
    including whether the answer was correct or incorrect.

    Attributes
    ----------
    santri : ForeignKey
        The related `Santri` who answered the question.
    soal : ForeignKey
        The related `Soal` that was answered.
    jawaban_santri : CharField
        The letter representing the student's chosen answer (A/B/C/D).
    is_correct : BooleanField
        Indicates whether the student's answer was correct.

    Methods
    -------
    __str__()
        Returns a formatted string like "<Student Name> - <Question ID>".
    """
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    soal = models.ForeignKey(Soal, on_delete=models.CASCADE)
    jawaban_santri = models.CharField(max_length=1)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.santri.nama} - {self.soal.id}"


class Nilai(models.Model):
    """
    Model representing the final score of a student.

    The score is calculated based on the number of correct answers
    from the evaluations and includes the total time taken in seconds.

    Attributes
    ----------
    santri : OneToOneField
        A one-to-one relationship to the `Santri` model. Each student has only one final score.
    nilai_akhir : FloatField
        The final score on a 0–100 scale.
    tanggal : DateTimeField
        Automatically stores the timestamp when the record was first created.
    durasi_detik : IntegerField
        The duration of the evaluation process in seconds.

    Methods
    -------
    __str__()
        Returns a formatted string like "<Student Name> - <Final Score>".
    """
    santri = models.OneToOneField(Santri, on_delete=models.CASCADE)
    nilai_akhir = models.FloatField()
    tanggal = models.DateTimeField(auto_now_add=True)
    durasi_detik = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.santri.nama} - {self.nilai_akhir}"
