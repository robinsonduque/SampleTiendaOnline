from email.headerregistry import ContentDispositionHeader
from django.db import models

# Create your models here.
class Servicios(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    contenido = models.CharField(max_length=80)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
