from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    fecha_nac=models.DateField((""), auto_now=False, auto_now_add=False)
    domicilio=models.CharField(max_length=6)
    curp=models.CharField(max_length=6)

    def __str__(self):
        return self.nombre