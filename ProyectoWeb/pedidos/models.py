from django.db import models
from django.contrib.auth import get_user_model
from ProyectoWebTienda.models import Productos
from django.db.models import Sum, F, FloatField


# Create your models here.
User = get_user_model()


class Pedidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "" + str(self.id)


""" @property
    def total(self):
        return self.DetallePedidos_set.aggregate(
            total=Sum(F("precion") * F("cantidad"), output_field=FloatField)
        )["total"]"""


class DetallePedidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cantidad: %s, Producto: %s" % (self.cantidad, self.producto.nombre)
