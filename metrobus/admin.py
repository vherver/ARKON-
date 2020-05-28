from django.contrib import admin

from metrobus.models import UpdateInformation, MetrobusUnitInformation



class InformationAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('id', 'information_date',)


class MetrobusAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('id', 'information_date', 'vehicle_id', 'position_longitude', 'position_latitude', 'alcaldia')


admin.site.register(UpdateInformation, InformationAdmin)
admin.site.register(MetrobusUnitInformation, MetrobusAdmin)