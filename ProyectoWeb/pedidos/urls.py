from django.urls import path
from .views import procesarPedido

urlpatterns = [
    path("procesarPedido", procesarPedido, name="procesarPedido"),
]
