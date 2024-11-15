from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.

def Inicio_VistaEmpleado(request):
    ElEmpleados=Empleado.objects.all()
    return render(request, "GestionarEmpleado.html",{"LosEmpleados":ElEmpleados})

def RegistarEmpleado(request):
    Id_Empleado=request.POST["txtId_Empleado"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Salario=request.POST["numSalario"]
    Fecha_Nacimiento=request.POST["txtFecha_Nacimiento"]
    CRP=request.POST["numCRP"]
    RFC=request.POST["numRFC"]


    GuardarEmpleado=Empleado.objects.create(
        Id_Empleado=Id_Empleado, Nombre=Nombre, Apellido=Apellido, Salario=Salario, Fecha_Nacimiento=Fecha_Nacimiento, CRP=CRP, RFC=RFC
    ) # Guarda el Registro
    return redirect("/")

def SeleccionarEmpleado(request,Id_Empleado):
    empleado=Empleado.objects.get(Id_Empleado=Id_Empleado)
    return render(request,"EditarEmpleado.html",{"LosEmpleados":empleado})

def EditarEmpleado(request):
    Id_Empleado=request.POST["txtId_Empleado"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Salario=request.POST["numSalario"]
    Fecha_Nacimiento=request.POST["txtFecha_Nacimiento"]
    CRP=request.POST["numCRP"]
    RFC=request.POST["numRFC"]
    empleado=Empleado.objects.get(Id_Empleado=Id_Empleado)
    empleado.Nombre=Nombre
    empleado.Apellido=Apellido
    empleado.Salario=Salario
    empleado.Fecha_Nacimiento=Fecha_Nacimiento
    empleado.CRP=CRP
    empleado=RFC=RFC
    empleado.save #Guarda Registro Actualizado
    return redirect("/")

def BorrarEmpleado(request,Id_Empleado):
    empleado=Empleado.objects.get(Id_Empleado=Id_Empleado)
    empleado.delete() #Borrar El Registro
    return redirect("/")

    