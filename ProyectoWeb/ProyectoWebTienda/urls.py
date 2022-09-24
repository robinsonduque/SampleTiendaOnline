from django.urls import path
from ProyectoWebTienda.views import *

urlpatterns = [
    path("tienda", tienda, name="tienda"),
]
