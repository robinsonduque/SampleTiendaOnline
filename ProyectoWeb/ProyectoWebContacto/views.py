from django.shortcuts import render, redirect
from .forms import ContactoForm


# Create your views here.
def contacto(request):
    formulario = ContactoForm()

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            message = request.POST.get("message")

            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {"formulario": formulario})
