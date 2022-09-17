from django.urls import path
from ProyectoWebBlog.views import *

urlpatterns = [
    path("blog/<categoria_id>", blog, name="blog"),
    path("blog/", blog, name="blog"),
]
