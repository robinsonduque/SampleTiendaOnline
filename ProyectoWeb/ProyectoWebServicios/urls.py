from django.urls import path
from ProyectoWebServicios.views import *

urlpatterns = [
    path("servicios", servicios, name="servicios"),
]
