from django import forms

class EvaluasiForm(forms.Form):
    def __init__(self, *args, soal_list=None, **kwargs):
        super().__init__(*args, **kwargs)
        if soal_list:
            for soal in soal_list:
                pilihan = soal.pilihan.all()
                
                choices = []
                for c in pilihan:
                    val = str(c.kode_pilihan) if isinstance(
                        c.kode_pilihan, tuple) else c.kode_pilihan
                    choices.append((val, c.teks_pilihan))

                self.fields[f'jawaban_{soal.id}'] = forms.ChoiceField(
                    label=soal.teks_soal,
                    choices=choices,
                    widget=forms.RadioSelect,
                    required=True
                )

        self.fields['durasi_detik'] = forms.IntegerField(
            widget=forms.HiddenInput(), required=False)


