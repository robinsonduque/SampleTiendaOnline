from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True, blank=True
    )
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
