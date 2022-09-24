from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def contacto(request):
    formulario = ContactoForm()

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            message = request.POST.get("mensaje")
            recipient_list = ["robinson.duque@correounivalle.edu.co"]

            email = EmailMessage(
                "Mensaje de la app de Django",
                "El usuario con nombre {} y la direccion {} dice: {}".format(
                    nombre, email, message
                ),
                "",
                recipient_list,
            )
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?NOvalido")

    return render(request, "contacto/contacto.html", {"formulario": formulario})
