from django.shortcuts import render, HttpResponse
from .models import Categoria, Post


# Create your views here.


# def blog(request):
#    categorias = Categoria.objects.all()
#    posts = Post.objects.all()
#    return render(request, "blog/blog.html", {"categorias": categorias, "posts": posts})


def blog(request, categoria_id="all"):
    categorias = Categoria.objects.all()
    posts = ""
    categoriaFiltrada = ""
    if categoria_id == "all":
        posts = Post.objects.all()
    else:
        categoriaFiltrada = Categoria.objects.get(id=categoria_id)
        posts = Post.objects.filter(categorias=categoriaFiltrada)

    return render(
        request,
        "blog/blog.html",
        {"categorias": categorias, "posts": posts, "filtro": categoriaFiltrada},
    )
