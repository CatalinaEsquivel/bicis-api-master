from django.urls import path
from rest_bicicleta.views import lista_bicicletas, detalle_bicicleta

urlpatterns = [
    path('lista_bicicletas',lista_bicicletas,name="lista_bicicletas"),
    path('detalle_bicicleta/<id>',detalle_bicicleta,name="detalle_bicicleta"),
]