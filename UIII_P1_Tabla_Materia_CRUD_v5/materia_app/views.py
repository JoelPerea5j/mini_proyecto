from django.shortcuts import render, redirect
from .models import Materia
# Create your views here.

def Inicio_Vista(request):
    lasMaterias=Materia.objects.all()
    return render(request, "GestionarMateria.html",{"MisMaterias":lasMaterias})

def RegistarMateria(request):
    Codigo=request.POST["txtCodigo"]
    Nombre=request.POST["txtNombre"]
    Creditos=request.POST["numCreditos"]

    GuardarMateria=Materia.objects.create(
        Codigo=Codigo, Nombre=Nombre, Creditos=Creditos
    ) # Guarda el Registro
    return redirect("/")

def SeleccionarMateria(request,Codigo):
    materia=Materia.objects.get(Codigo=Codigo)
    return render(request,"editarmateria.html",{"MisMaterias":materia})

def EditarMateria(request):
    Codigo=request.POST["txtCodigo"]
    Nombre=request.POST["txtNombre"]
    Creditos=request.POST["numCreditos"]
    materia=Materia.objects.get(Codigo=Codigo)
    materia.Nombre=Nombre
    materia.Creditos=Creditos
    materia.save() #Guarda Registro Actualizado
    return redirect("/")

def BorrarMateria(request,Codigo):
    materia=Materia.objects.get(Codigo=Codigo)
    materia.delete() #Borrar El Registro
    return redirect("/")

    