from django.db import models
from django.contrib.auth.models import User


class Tienda(models.Model):
    direccion = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    fechacreacion = models.DateField(auto_now_add=True)
    telefonocontacto = models.CharField(max_length=10, blank=True, null=True)
