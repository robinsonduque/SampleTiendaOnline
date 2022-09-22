from django.urls import path
from ProyectoWebBlog.views import *

urlpatterns = [
    path("blog/<categoria_id>", blog, name="blogCategoria"),
    path("blog/", blog, name="blog"),
    path("evaluar/", evaluarCodigo, name="evaluar"),
]
