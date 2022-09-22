from django.shortcuts import render
from django.http import HttpResponse
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


import subprocess
from subprocess import check_output
import traceback
import sys


def evaluarCodigo(request):
    try:
        res = check_output(
            [
                "/Applications/Racket v7.9/bin/racket",
                "/Applications/Racket v7.9/bin/hello.rkt",
                "-n",
                "x",
            ],
            timeout=5,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as e:

        res = (
            "Error:"
            + str(e.output).replace("\\n", "<br>")
            + "<br> or Timeout after 5 seconds"
        )

    return HttpResponse("%s" % res)
