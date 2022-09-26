from django.shortcuts import render, HttpResponse

from .models import Productos, Categoria

# Create your views here.


def tienda(request, categoria_id="all"):
    categorias = Categoria.objects.all()
    productos = ""
    categoriaFiltrada = ""
    if categoria_id == "all":
        productos = Productos.objects.all()
    else:
        categoriaFiltrada = Categoria.objects.get(id=categoria_id)
        productos = Productos.objects.filter(categoria=categoriaFiltrada)

    return render(
        request,
        "tienda/tienda.html",
        {"productos": productos, "categorias": categorias, "filtro": categoriaFiltrada},
    )
