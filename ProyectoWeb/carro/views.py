from django.shortcuts import render, redirect
from .carro import Carro
from ProyectoWebTienda.models import Producto

# Create your views here.


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.object.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")
