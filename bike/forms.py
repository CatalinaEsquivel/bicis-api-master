from django import forms
from django.forms import ModelForm
from .models import Bicicleta

class BicicletaForm(ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['idBicicleta', 'marca', 'imagen', 'descripcionBicicleta', 'precio', 'tipoBicicleta']