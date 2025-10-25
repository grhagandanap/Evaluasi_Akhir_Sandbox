from django.contrib.auth.models import User
from eas.models import Santri
import random
import string

# --- Fungsi bantu ---
def generate_username(nama):
    base = ''.join(nama.split()).lower()  # hapus spasi, lowercase
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{base}{suffix}"


def generate_password():
    # Password default untuk semua santri (bisa diubah di admin)
    return "santri123"


# --- Proses ---
santri_list = Santri.objects.all()

for santri in santri_list:
    # Cek apakah sudah punya user
    if hasattr(santri, 'user') and santri.user:
        print(f"⚠️ {santri.nama} sudah punya user ({santri.user.username}), skip.")
        continue

    # Buat user baru
    username = generate_username(santri.nama)
    password = generate_password()
    user = User.objects.create_user(username=username, password=password)

    # Hubungkan user ke santri
    santri.user = user
    santri.save()

    print(f"{santri.nama} → username: {username} | password: {password}")

print("\nSemua akun santri berhasil dibuat dan terhubung dengan User.")
