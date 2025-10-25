from django.contrib import admin
from .models import Santri, Nilai, Soal, PilihanJawaban, Evaluasi

# Optional: Customize how models appear in the admin
class SantriAdmin(admin.ModelAdmin):
    list_display = ('santri_id', 'nama', 'usia', 'gender', 'get_username')
    search_fields = ('nama',)

    def get_username(self, obj):
        return obj.user.username if obj.user else "-"
    get_username.short_description = 'Username'

class SoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'teks_soal', 'jawaban_benar')
    search_fields = ('teks_soal',)

class PilihanJawabanAdmin(admin.ModelAdmin):
    list_display = ('soal', 'kode_pilihan', 'teks_pilihan')
    list_filter = ('soal',)

# Register your models here.
admin.site.register(Santri, SantriAdmin)
admin.site.register(Nilai)
admin.site.register(Soal, SoalAdmin)
admin.site.register(PilihanJawaban, PilihanJawabanAdmin)
admin.site.register(Evaluasi)

