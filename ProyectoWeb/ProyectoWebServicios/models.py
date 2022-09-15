from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from django.db import models

# Create your models here.
class Servicios(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    contenido = models.CharField(max_length=80)
    imagen = models.ImageField(
        upload_to="servicios"
    )  # se configuró en settings para que cargue las imagenes en este directorio
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
