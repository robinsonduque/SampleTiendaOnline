from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=80)
    contenido = models.CharField(max_length=80)
    imagen = models.ImageField(
        upload_to="blog", null=True, blank=True
    )  # se configuró en settings para que cargue las imagenes en este directorio
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
