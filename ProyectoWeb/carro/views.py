from django.shortcuts import render, redirect, HttpResponse
from .carro import Carro
from ProyectoWebTienda.models import Productos
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required  # para esto se configura la variable LOGIN_URL
def agregar(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")
    # return HttpResponse("hola carro")


def eliminar(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.eliminar_producto(producto=producto)
    return redirect("tienda")


def restar(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")


def sumar(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")
