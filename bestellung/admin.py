from django.contrib import admin
from .models import Lieferant, Lieferung, Artikel, Lieferposition, Lagerplatz

# Register your models here.

admin.site.register(Lieferant)
admin.site.register(Lieferung)
# admin.site.register(Artikel)
admin.site.register(Lieferposition)
# admin.site.register(Lagerplatz)


#adds a searchfield 
@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    search_fields = ['bezeichnung', 'bemerkung'] #adds a searchfield

    list_display = ['bezeichnung', 'liefereinheit', 'ekpreis'] #adds columns 


@admin.register(Lagerplatz)
class LagerplatzAdmin(admin.ModelAdmin):
    list_filter = ['artikel'] #adds list with filter on the site 