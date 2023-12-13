from django.db import models
from tiendas.models import Tienda


class Producto(models.Model):
    descripcion = models.CharField(max_length=400, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    tiendafk = models.ForeignKey(Tienda, on_delete=models.SET_NULL, null=True)
