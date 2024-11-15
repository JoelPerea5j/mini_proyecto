from django.urls import path
from Empleados_app import views

urlpatterns = [
    path("",views.Inicio_VistaEmpleado, name="Inicio_VistaEmpleado"),
    path("RegistarEmpleado/",views.RegistarEmpleado,name="RegistarEmpleado"),
    path("SeleccionarEmpleado/<ID_Empleado>",views.SeleccionarEmpleado,name="SeleccionarEmpleado"),
    path("EditarEmpleado/",views.EditarEmpleado,name="EditarEmpleado"),
    path("BorrarEmpleado/<ID_Empleado>",views.BorrarEmpleado,name="BorrarEmpleado")
]
