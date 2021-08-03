from core.models import Categoria, Vehiculo
from django.contrib import admin
from .models import Categoria, Vehiculo

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Vehiculo)