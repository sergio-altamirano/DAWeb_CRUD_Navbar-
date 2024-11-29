from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=6)
    horario=models.CharField(max_length=100)
    num_trabajadores=models.CharField(max_length=6)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)
    id_ventas=models.CharField(max_length=6)
    correo=models.CharField(max_length=100)



    def __str__(self):
        return self.direcccion