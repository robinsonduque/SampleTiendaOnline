from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ProyectoWebTienda.models import Productos
from carro.carro import Carro
from pedidos.models import DetallePedidos, Pedidos

# Create your views here.
@login_required(login_url="iniciar_sesion/")
def procesarPedido(request):

    pedido = Pedidos.objects.create(user=request.user)
    carro = Carro(request)
    lista_productos = []
    for key, prod in carro.carro.items():
        lista_productos.append(
            DetallePedidos(
                user=request.user,
                producto=Productos.objects.get(id=prod["producto_id"]),
                pedido=pedido,
                cantidad=prod["cantidad"],
            )
        )
    DetallePedidos.objects.bulk_create(lista_productos)

    enviar_mail(
        pedido=pedido,
        detalle=lista_productos,
        nombreUsuario=request.user.username,
        email=request.user.email,
    )

    messages.success(request, "El pedido ha sido creado exitosamente")

    return redirect("tienda")


def enviar_mail(pedido, detalle, nombreUsuario, email):
    pass
