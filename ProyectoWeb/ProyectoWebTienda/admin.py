from django.contrib import admin

# Register your models here.

from ProyectoWebTienda.models import Productos

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "created")
    readonly_fields = ("created", "updated")


admin.site.register(Productos, ProductosAdmin)
