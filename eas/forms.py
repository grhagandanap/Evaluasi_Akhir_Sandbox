from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Username atau password tidak sesuai. "
            "Pastikan Anda mengetik dengan benar (huruf besar/kecil diperhatikan)."
        ),
    }

class EvaluasiForm(forms.Form):
    """
    Form dinamis untuk evaluasi (kuis) santri.

    Form ini dibuat secara dinamis berdasarkan daftar soal (`soal_list`) yang diberikan saat inisialisasi.
    Untuk setiap soal, form akan men-generate satu field pilihan jawaban (ChoiceField)
    dengan opsi radio button (A, B, C, D).  
    Selain itu, form juga menyertakan field tersembunyi `durasi_detik` untuk menyimpan
    waktu pengerjaan evaluasi dalam satuan detik.

    Parameters
    ----------
    *args : tuple
        Argumen standar untuk inisialisasi form Django.
    soal_list : list of Soal, optional
        Daftar objek `Soal` yang akan digunakan untuk membentuk field dinamis.
        Setiap `Soal` diasumsikan memiliki relasi ke model `PilihanJawaban`.
    **kwargs : dict
        Keyword arguments tambahan untuk `forms.Form`.

    Attributes
    ----------
    jawaban_<soal.id> : ChoiceField
        Field pilihan jawaban untuk setiap soal yang di-generate secara dinamis.
        Label field berisi teks soal, dan opsinya diambil dari model `PilihanJawaban`.
    durasi_detik : IntegerField
        Field tersembunyi (HiddenInput) untuk menyimpan lama waktu pengerjaan (detik).

    Example
    -------
    >>> from evaluasi.models import Soal
    >>> soal_list = Soal.objects.all()[:4]
    >>> form = EvaluasiForm(soal_list=soal_list)
    >>> form.fields.keys()
    dict_keys(['jawaban_1', 'jawaban_2', 'jawaban_3', 'jawaban_4', 'durasi_detik'])

    Notes
    -----
    - Field `durasi_detik` diisi dari JavaScript timer di template frontend.
    - Setiap field `jawaban_<soal.id>` wajib diisi (`required=True`).
    """

    def __init__(self, *args, soal_list=None, **kwargs):
        """
        Inisialisasi form evaluasi.

        Membangun field-field dinamis berdasarkan daftar soal (`soal_list`).
        Setiap field memiliki label teks soal dan pilihan jawaban (A–D)
        yang diambil dari relasi `soal.pilihan`.

        Parameters
        ----------
        *args : tuple
            Argumen standar untuk form Django.
        soal_list : list of Soal, optional
            Daftar soal untuk membentuk field dinamis.
        **kwargs : dict
            Keyword arguments tambahan.
        """
        super().__init__(*args, **kwargs)
        if soal_list:
            for soal in soal_list:
                pilihan = soal.pilihan.all()

                choices = []
                for c in pilihan:
                    # Ambil kode pilihan (A/B/C/D) dan teks pilihan
                    val = str(c.kode_pilihan) if isinstance(
                        c.kode_pilihan, tuple) else c.kode_pilihan
                    choices.append((val, c.teks_pilihan))

                # Tambahkan field dinamis untuk setiap soal
                self.fields[f'jawaban_{soal.id}'] = forms.ChoiceField(
                    label=soal.teks_soal,
                    choices=choices,
                    widget=forms.RadioSelect,
                    required=True
                )

        # Tambahkan field tersembunyi untuk durasi pengerjaan
        self.fields['durasi_detik'] = forms.IntegerField(
            widget=forms.HiddenInput(),
            required=False
        )
