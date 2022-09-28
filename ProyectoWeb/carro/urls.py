from django.urls import path
from carro.views import agregar, eliminar, restar

app_name = "carro"

urlpatterns = [
    path("agregarproducto/<int:producto_id>", agregar, name="agregarproducto"),
    path("restarproducto/<int:producto_id>", restar, name="restarproducto"),
    # path("tienda/<categoria_id>", tienda, name="tiendaCategoria"),
]
