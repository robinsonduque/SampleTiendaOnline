from django.contrib import admin

# Register your models here.

from ProyectoWebTienda.models import Productos, Categoria

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "created")
    readonly_fields = ("created", "updated")


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    readonly_fields = ("created", "updated")


admin.site.register(Productos, ProductosAdmin)
admin.site.register(Categoria, CategoriaAdmin)
