from django.db import models

# Create your models here.


class Ventas(models.Model):
    id_venta=models.SmallIntegerField(primary_key=True)
    id_producto=models.SmallIntegerField()
    id_cliente=models.SmallIntegerField()
    fecha_venta=models.DateField()
    id_sucursal=models.SmallIntegerField()
    cantidad=models.SmallIntegerField()
    pago=models.CharField(max_length=50)

    def __str__(self):
        return self.pago