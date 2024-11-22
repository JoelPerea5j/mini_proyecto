from django.urls import path
from Empleado_app import views

urlpatterns = [
    path("",views.Inicio_Vista, name="Inicio_Vista"),
    path("RegistarEmpleado/",views.RegistarEmpleado,name="RegistarEmpleado"),
    path("SeleccionarEmpleado/<Id_Empleado>",views.SeleccionarEmpleado,name="SeleccionarEmpleado"),
    path("EditarEmpleado/",views.EditarEmpleado,name="EditarEmpleado"),
    path("BorrarEmpleado/<Id_Empleado>",views.BorrarEmpleado,name="BorrarEmpleado")
]
