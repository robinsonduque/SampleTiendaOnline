from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
