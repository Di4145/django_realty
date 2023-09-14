from django.contrib import admin

import realtys.models


class RealtyAdmin(admin.ModelAdmin):
    list_display = ('type', 'cost')


# Register your models here.

admin.site.register(realtys.models.Realty, RealtyAdmin)
admin.site.register(realtys.models.RealtyType)
admin.site.register(realtys.models.RealtyManager)
admin.site.register(realtys.models.Bill)