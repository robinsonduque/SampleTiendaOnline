from django.urls import path
from ProyectoWebApp.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("tienda", tienda, name="tienda"),
    path("servicios", servicios, name="servicios"),
    path("contacto", contacto, name="contacto"),
    path("blog", blog, name="blog"),
]
