from core.forms import VehiculosForm
from .models import Vehiculo
from django.shortcuts import redirect, render

# Create your views here.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()


def home(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        "vehiculos" : vehiculos
    }
    return render(request, 'core/home.html', datos)

def form_vehiculos(request):
    datos = {
        'form' : VehiculosForm()
    }

    if request.method == 'POST':
        formulario = VehiculosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_vehiculo.html', datos)


def form_mod_vehiculo(request, id):
    # El id es el identificador de la tabla vehiculos
    # Buscamos los datos en la base de datos
    # Buscamos con el id que llega desde la url

    vehiculo = Vehiculo.objects.get(patente=id)

    datos = {
        'form' : VehiculosForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculosForm(request.POST, instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/form_mod_vehiculo.html', datos)


def form_del_vehiculo(request, id):

    vehiculo = Vehiculo.objects.get(patente=id)

    vehiculo.delete()
    
    return redirect(to="home")

def prueba(request):
    return render(request, 'core/prueba.html')    

def opcion1(request):
    data = {
        "titulo" : "Opcion 1"
    }
    return render(request, 'core/opcion1.html', data)        