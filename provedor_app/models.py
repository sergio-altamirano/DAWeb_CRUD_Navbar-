from django.db import models

# Create your models here.

class Provedor(models.Model):
    id_provedor=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    tipo_entrega=models.CharField(max_length=100)
    dia_entrega=models.DateField((""), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nombre