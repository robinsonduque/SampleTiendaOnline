from django.urls import path
from .views import Registro


app_name = "autenticacion"

urlpatterns = [
    path("autenticar/", Registro.as_view(), name="registrar"),
]
