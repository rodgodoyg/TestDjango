from django.forms import ModelForm
from .models import Vehiculo

class VehiculosForm(ModelForm):

    
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria']