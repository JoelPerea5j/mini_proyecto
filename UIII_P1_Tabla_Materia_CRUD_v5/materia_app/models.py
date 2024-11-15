from django.db import models

# Create your models here.
class Materia(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=100)
    Creditos=models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.Nombre