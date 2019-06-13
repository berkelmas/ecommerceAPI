from django.contrib import admin
from .models import Urun, Kategori, Marka, Varyant, Siparis

class UrunAdmin(admin.ModelAdmin):
    filter_horizontal = ('varyant',)
admin.site.register(Urun, UrunAdmin);

class KategoriAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kategori, KategoriAdmin)

class MarkaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Marka, MarkaAdmin)

class VaryantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Varyant, VaryantAdmin)

class SiparisAdmin(admin.ModelAdmin):
    pass
admin.site.register(Siparis, SiparisAdmin)
