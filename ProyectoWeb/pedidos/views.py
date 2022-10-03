from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ProyectoWebTienda.models import Productos
from carro.carro import Carro
from pedidos.models import DetallePedidos, Pedidos
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings

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


def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string(
        "mensaje/mensaje_pedido.html",
        {
            "pedido": kwargs.get("pedido"),
            "detalle": kwargs.get("detalle"),
            "nombreUsuario": kwargs.get("nombreUsuario"),
            "usuarioMail": kwargs.get("email"),
        },
    )
    mensaje_texto = strip_tags(mensaje)
    from_email = settings.EMAIL_HOST_USER
    to = kwargs.get("email")
    # print(mensaje_texto)
    # send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
