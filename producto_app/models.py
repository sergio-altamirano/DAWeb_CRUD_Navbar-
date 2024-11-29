from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)
    cantidad=models.CharField(max_length=100)
    id_ingrediente=models.CharField(max_length=6)
    id_sucursal=models.CharField(max_length=6)
    Id_categoria=models.CharField(max_length=6)

    def __str__(self):
        return self.nombre