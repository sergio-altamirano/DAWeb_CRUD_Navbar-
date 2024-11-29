from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    id_ingrediente=models.CharField(primary_key=True,max_length=6)
    id_provedor=models.CharField(max_length=6)
    id_producto=models.CharField(max_length=6)
    tipo_carne=models.CharField(max_length=100)
    id_categoria=models.CharField(max_length=6)

    def __str__(self):
        return self.tipo_carne