"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from metrobus.api_v1.endpoints import *

app_name = 'metrobus_v1'


urlpatterns = [
    path(r'remoteInfo/', GetRemoteInfo.as_view(), name='Creacion de registros'),
    path(r'', MetrobusDisponibles.as_view(), name='Lista de Metrobus'),
    path(r'alcaldias/', Alcaldias.as_view(), name='Lista de Alcaldias'),
    path(r'alcaldias/<str:alcaldia_id>/', AlcaldiasUnit.as_view(), name='Regiistros por alcaldia'),
    path(r'<str:unit_id>/', InfoUnit.as_view(), name='Registros por metrobus'),

]
