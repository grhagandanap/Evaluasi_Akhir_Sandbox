from eas.models import Santri
import random
import string


def generate_santri_id(gender):
    # Y = 3 huruf random, X = 5 angka random
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=5))
    prefix = 'ARN' if gender == 'L' else 'ART'
    return f"{prefix}{letters}-{numbers}"


# Contoh nama
nama_laki = [
    "Ahmad Fauzan", "Rizky Hidayat", "Muhammad Yusuf", "Fajar Ramadhan", "Imam Arif",
    "Zaki Abdullah", "Rafli Akbar", "Rizal Hakim", "Hilmi Fadlan", "Hasan Al-Basri"
]

nama_perempuan = [
    "Aisyah Rahma", "Nurul Fadhilah", "Fatimah Zahra", "Siti Mariam", "Dina Khairunnisa",
    "Hafshah Aulia", "Khadijah Lestari", "Amira Zahra", "Laila Hanifah", "Salma Putri"
]

# Generate santri laki-laki
for nama in nama_laki:
    Santri.objects.create(
        santri_id=generate_santri_id('L'),
        nama=nama,
        usia=random.randint(13, 20),
        alamat=f"Jl. Pesantren No.{random.randint(1,99)}, Bandung",
        gender='I'
    )

# Generate santri perempuan
for nama in nama_perempuan:
    Santri.objects.create(
        santri_id=generate_santri_id('P'),
        nama=nama,
        usia=random.randint(13, 20),
        alamat=f"Jl. Pesantren No.{random.randint(1,99)}, Bandung",
        gender='A'
    )

print("✅ 20 santri dummy berhasil dibuat.")
