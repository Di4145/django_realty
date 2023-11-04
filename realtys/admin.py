from django.contrib import admin
import realtys.models

class GalleryInLines(admin.TabularInline):
    fk_name = 'realty'
    model = realtys.models.Gallery


class RealtyAdmin(admin.ModelAdmin):
    list_display = ('type', 'cost')
    inlines = [GalleryInLines]


# Register your models here.

admin.site.register(realtys.models.Realty, RealtyAdmin)
admin.site.register(realtys.models.RealtyType)
admin.site.register(realtys.models.RealtyManager)
admin.site.register(realtys.models.Bill)
admin.site.register(realtys.models.Gallery)
admin.site.register(realtys.models.Usd)