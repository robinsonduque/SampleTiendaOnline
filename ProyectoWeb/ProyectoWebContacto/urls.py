from django.urls import path
from ProyectoWebContacto.views import contacto

urlpatterns = [
    path("contacto/", contacto, name="contacto"),
]
