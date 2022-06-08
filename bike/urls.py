from django.conf import settings
from django.conf.urls.static import static
from xml.dom.minidom import Document
from django.urls import path
from .views import index, iniciosesion, registro, bicicletas, home, form_bicicleta, form_mod_bicicleta, form_de_bicicleta
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', index, name='admin-index'),
    path('bicicletas/', bicicletas, name='bicicletas'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('registro/', registro, name='registro'),
]

urlpatterns = [
    path('',home,name='home'),
    path('form_bicicleta',form_bicicleta,name="form_bicicleta"),
    path('modificar-bicicleta/<id>', form_mod_bicicleta, name="form_mod_bicicleta"),
    path('eliminar-bicicleta/<id>', form_de_bicicleta, name="form_de_bicicleta"),
]
