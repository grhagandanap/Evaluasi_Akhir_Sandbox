from eas.models import Soal, PilihanJawaban

# --- DATA SOAL ---
soal_data = [
    # --- Akidah ---
    {
        "teks_soal": "Siapakah yang berhak disembah dengan benar?",
        "jawaban_benar": "C",
        "pilihan": {
            "A": "Nabi dan orang saleh",
            "B": "Malaikat dan wali",
            "C": "Hanya Allah semata",
            "D": "Siapa saja yang diyakini memberi manfaat",
        },
    },
    {
        "teks_soal": "Apa makna kalimat Laa ilaaha illallah?",
        "jawaban_benar": "B",
        "pilihan": {
            "A": "Tidak ada Tuhan selain Allah secara nama",
            "B": "Tidak ada sesembahan berhak diibadahi dengan benar kecuali Allah",
            "C": "Tidak ada pencipta selain Allah",
            "D": "Tidak ada yang lebih tinggi dari Allah",
        },
    },
    {
        "teks_soal": "Siapa yang menciptakan langit dan bumi?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Allah",
            "B": "Malaikat",
            "C": "Nabi Adam",
            "D": "Manusia",
        },
    },
    {
        "teks_soal": "Apa yang dimaksud dengan tauhid uluhiyyah?",
        "jawaban_benar": "D",
        "pilihan": {
            "A": "Meyakini Allah sebagai Pencipta",
            "B": "Meyakini Allah sebagai Pemberi rezeki",
            "C": "Meyakini Allah memiliki nama dan sifat sempurna",
            "D": "Mengikhlaskan ibadah hanya kepada Allah",
        },
    },
    {
        "teks_soal": "Siapakah yang wajib diikuti dalam beragama?",
        "jawaban_benar": "C",
        "pilihan": {
            "A": "Ulama modern",
            "B": "Pemimpin negara",
            "C": "Rasulullah",
            "D": "Orang tua",
        },
    },

    # --- Fikih ---
    {
        "teks_soal": "Apa hukum shalat lima waktu bagi seorang Muslim?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Wajib",
            "B": "Sunnah",
            "C": "Mubah",
            "D": "Makruh",
        },
    },
    {
        "teks_soal": "Berapa kali seorang Muslim wajib menunaikan zakat fitrah dalam setahun?",
        "jawaban_benar": "B",
        "pilihan": {
            "A": "Dua kali",
            "B": "Satu kali",
            "C": "Setiap bulan",
            "D": "Setiap Jumat",
        },
    },
    {
        "teks_soal": "Apa yang membatalkan wudhu?",
        "jawaban_benar": "C",
        "pilihan": {
            "A": "Makan dan minum",
            "B": "Mengantuk",
            "C": "Keluar sesuatu dari dua jalan",
            "D": "Berjalan jauh",
        },
    },
    {
        "teks_soal": "Kapan waktu terbaik untuk melaksanakan shalat dhuha?",
        "jawaban_benar": "D",
        "pilihan": {
            "A": "Setelah Subuh",
            "B": "Menjelang Maghrib",
            "C": "Sebelum Subuh",
            "D": "Ketika matahari mulai meninggi",
        },
    },
    {
        "teks_soal": "Apa syarat sahnya puasa Ramadan?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Islam, baligh, berakal, dan suci dari haid (bagi wanita)",
            "B": "Berpuasa minimal 10 hari",
            "C": "Tidak makan setelah Subuh",
            "D": "Hanya menahan lapar",
        },
    },

    # --- Sirah Nabawiyah ---
    {
        "teks_soal": "Di mana Nabi Muhammad ﷺ lahir?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Mekkah",
            "B": "Madinah",
            "C": "Thaif",
            "D": "Syam",
        },
    },
    {
        "teks_soal": "Siapakah istri pertama Nabi Muhammad ﷺ?",
        "jawaban_benar": "B",
        "pilihan": {
            "A": "Aisyah r.a.",
            "B": "Khadijah r.a.",
            "C": "Hafshah r.a.",
            "D": "Ummu Salamah r.a.",
        },
    },
    {
        "teks_soal": "Berapa tahun Nabi berdakwah di Makkah?",
        "jawaban_benar": "C",
        "pilihan": {
            "A": "10 tahun",
            "B": "15 tahun",
            "C": "13 tahun",
            "D": "20 tahun",
        },
    },
    {
        "teks_soal": "Perang pertama yang terjadi dalam Islam adalah?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Perang Badar",
            "B": "Perang Uhud",
            "C": "Perang Khandaq",
            "D": "Perang Hunain",
        },
    },
    {
        "teks_soal": "Siapakah khalifah pertama setelah wafatnya Nabi Muhammad ﷺ?",
        "jawaban_benar": "D",
        "pilihan": {
            "A": "Umar bin Khattab",
            "B": "Utsman bin Affan",
            "C": "Ali bin Abi Thalib",
            "D": "Abu Bakar Ash-Shiddiq",
        },
    },

    # --- Fikih Muamalat ---
    {
        "teks_soal": "Apa hukum riba dalam Islam?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Haram",
            "B": "Makruh",
            "C": "Mubah",
            "D": "Sunnah",
        },
    },
    {
        "teks_soal": "Transaksi jual beli yang halal harus dilakukan dengan?",
        "jawaban_benar": "C",
        "pilihan": {
            "A": "Paksaan",
            "B": "Riba",
            "C": "Kerelaan kedua pihak",
            "D": "Janji semata",
        },
    },
    {
        "teks_soal": "Apa hukum menjual barang yang belum dimiliki?",
        "jawaban_benar": "B",
        "pilihan": {
            "A": "Halal",
            "B": "Dilarang",
            "C": "Makruh",
            "D": "Boleh dengan syarat",
        },
    },
    {
        "teks_soal": "Bagaimana Islam mengatur akad dalam muamalah?",
        "jawaban_benar": "D",
        "pilihan": {
            "A": "Bebas tanpa syarat",
            "B": "Harus tertulis",
            "C": "Boleh dengan sumpah",
            "D": "Harus berdasarkan kerelaan dan kejelasan akad",
        },
    },
    {
        "teks_soal": "Apa syarat sahnya akad jual beli?",
        "jawaban_benar": "A",
        "pilihan": {
            "A": "Adanya penjual, pembeli, barang, dan kerelaan",
            "B": "Dilakukan di masjid",
            "C": "Dengan saksi minimal dua orang",
            "D": "Dilakukan pada hari Jumat",
        },
    },
]

# --- PROSES INPUT ---
for item in soal_data:
    soal = Soal.objects.create(
        teks_soal=item["teks_soal"],
        jawaban_benar=item["jawaban_benar"]
    )

    for kode, teks in item["pilihan"].items():
        PilihanJawaban.objects.create(
            soal=soal,
            kode_pilihan=kode,
            teks_pilihan=teks
        )

print("✅ 20 soal dan pilihan jawaban berhasil ditambahkan ke database!")
