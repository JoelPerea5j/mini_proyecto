from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.

def Inicio_Vista(request):
    LosEmpleados=Empleado.objects.all()
    return render(request, "GestionarEmpleado.html",{"ElEmpleado":LosEmpleados})

def RegistarEmpleado(request):
    Id_Empleado=request.POST["txid"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["numApellido"]
    Salario=request.POST["numSalario"]
    Fecha_Nacimiento=request.POST["numFecha"]
    CRP=request.POST["numCRP"]
    RFC=request.POST["numRFC"]

    GuardarMateria=Empleado.objects.create(
        Id_Empleado=Id_Empleado, Nombre=Nombre, Apellido=Apellido, Salario=Salario, Fecha_Nacimiento=Fecha_Nacimiento, CRP=CRP, RFC=RFC
    ) # Guarda el Registro
    return redirect("/")

def SeleccionarEmpleado(request,Id_Empleado):
    empleado=Empleado.objects.get(Id_Empleado=Id_Empleado)
    return render(request,".html",{"ElEmpleado":empleado})

def EditarEmpleado(request):
    Id_Empleado=request.POST["txid"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["numApellido"]
    Salario=request.POST["numSalario"]
    Fecha_Nacimiento=request.POST["numFecha"]
    CRP=request.POST["numCRP"]
    RFC=request.POST["numRFC"]

    empleado=Empleado.objects.get(Id_Empleado=Id_Empleado)
    empleado.Nombre=Nombre
    empleado.Apellido=Apellido
    empleado.Salario=Salario
    empleado.Fecha_Nacimiento=Fecha_Nacimiento
    empleado.CRP=CRP
    empleado.RFC=RFC
    empleado.save() #Guarda Registro Actualizado
    return redirect("/")

def BorrarEmpleado(request,Id_Empleado):
    empleado=Empleado.objects.get(Id_Empleado=Id_Empleado)
    empleado.delete() #Borrar El Registro
    return redirect("/")

    