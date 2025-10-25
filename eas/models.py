from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Santri(models.Model):
    GENDER_CHOICES = [
        ('I', 'Ikhwan'),
        ('A', 'Akhwat'),
    ]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True) 
    nama = models.CharField(max_length=100)
    santri_id = models.CharField(
        max_length=12, unique=True, default="ARX000-00000")
    usia = models.IntegerField()
    alamat = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.nama


class Soal(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    teks_soal = models.TextField()
    jawaban_benar = models.CharField(max_length=1, choices=GRADE_CHOICES)

    def __str__(self):
        return self.teks_soal


class PilihanJawaban(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    soal = models.ForeignKey(Soal, on_delete=models.CASCADE, related_name='pilihan')
    kode_pilihan = models.CharField(max_length=1, choices=Soal.GRADE_CHOICES)
    teks_pilihan = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.kode_pilihan}. {self.teks_pilihan}"

# d. Evaluasi (anak dari Santri, Soal, jawaban)
class Evaluasi(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    soal = models.ForeignKey(Soal, on_delete=models.CASCADE)
    jawaban_santri = models.CharField(max_length=1)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.santri.nama} - {self.soal.id}"

# e. Nilai (anak dari Santri)
class Nilai(models.Model):
    santri = models.OneToOneField(Santri, on_delete=models.CASCADE)
    nilai_akhir = models.FloatField()
    tanggal = models.DateTimeField(auto_now_add=True)
    durasi_detik = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.santri.nama} - {self.nilai_akhir}"
