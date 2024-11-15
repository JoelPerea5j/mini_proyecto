from django.urls import path
from materia_app import views

urlpatterns = [
    path("",views.Inicio_Vista, name="Inicio_Vista"),
    path("RegistarMateria/",views.RegistarMateria,name="RegistarMateria"),
    path("SeleccionarMateria/<Codigo>",views.SeleccionarMateria,name="SeleccionarMateria"),
    path("EditarMateria/",views.EditarMateria,name="EditarMateria"),
    path("BorrarMateria/<Codigo>",views.BorrarMateria,name="BorrarMateria")
]
