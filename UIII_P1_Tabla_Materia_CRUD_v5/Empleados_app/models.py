from django.db import models

# Create your models here.
class Empleado(models.Model):
    Id_Empleado=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Salario=models.PositiveBigIntegerField()
    Fecha_Nacimiento=models.CharField(max_length=100)
    CRP=models.PositiveBigIntegerField()
    RFC=models.PositiveBigIntegerField()

    
    def __str__(self) -> str:
        return self.Nombre


