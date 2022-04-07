from django.contrib import admin
from .models import Produkty, Zamówienia,Zwrot

admin.site.register(Produkty)
admin.site.register(Zamówienia)

admin.site.register(Zwrot)


class ProduktyAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'categoria', 'quatity', 'slug')
    list_filter = ['zniszczony']
    prepopulated_fields = {'slug': ('nazwa',)}
