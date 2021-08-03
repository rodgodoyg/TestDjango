from django.urls import path
from .views import form_vehiculos, home, opcion1, prueba, form_mod_vehiculo, form_del_vehiculo

urlpatterns = [
    path('', home, name="home"),
    path('prueba', prueba, name="prueba"),
    path('opcion1', opcion1, name="opcion1"),
    path('form-vehiculo', form_vehiculos, name="form_vehiculo"),
    path('form-mod-vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),
    

]