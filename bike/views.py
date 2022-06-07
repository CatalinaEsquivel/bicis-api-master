from ast import Return
from django.shortcuts import render, redirect
from .models import Bicicleta
from .forms import BicicletaForm

# Create your views here.
def index(request):
    return render(request,'bicicleta/index.html')

def bicicletas(request):
    return render(request,'bicicleta/bicicletas.html')

def iniciosesion(request):
    return render(request,'bicicleta/iniciosesion.html')

def registro(request):
    return render(request,'bicicleta/registro.html')

def home(request):
    datos = {
        'bicicletas':Bicicleta.objects.all()
    }
    ListaBicicletas = Bicicleta.objects.all()
    datos = {'bicicletas':ListaBicicletas}
    return render(request, 'bicicleta/index.html',datos)

def form_bicicleta(request):
    form = BicicletaForm()
    return render(request, 'bicicleta/form_bicicleta.html',{'form':form})

def form_bicicleta(request):
    datos = {
        'form':BicicletaForm()
    } 
    if(request.method == 'POST'):
        bicicleta = BicicletaForm(request.POST, files=request.FILES)
        if bicicleta.is_valid():
            bicicleta.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request, 'bicicleta/form_bicicleta.html', datos)

def form_mod_bicicleta(request, id):
    bicicleta = Bicicleta.objects.get(idBicicleta=id)
    
    datos = {
        'form':BicicletaForm(instance=bicicleta)
    }
    
    if request.method == 'POST':
        bicicleta = BicicletaForm(data = request.POST, instance = bicicleta, files=request.FILES)

        if bicicleta.is_valid():
            bicicleta.save() #modificar a la BD
            datos['mensaje'] = 'Se modificó Bicicleta'
        else:
            datos['mensaje'] = 'NO se modificó Bicicleta'
    
    return render(request, 'bicicleta/form_mod_bicicleta.html', datos)

def form_de_bicicleta(request, id):
    bicicleta = Bicicleta.objects.get(idBicicleta=id)
    bicicleta.delete()
    
    return redirect(to='home')