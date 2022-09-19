from django.shortcuts import render
from .models import Servicios

# Create your views here.


def servicios(request):
    todos = Servicios.objects.all()
    context = {"servicios": todos}
    return render(request, "servicios/servicios.html", context)
