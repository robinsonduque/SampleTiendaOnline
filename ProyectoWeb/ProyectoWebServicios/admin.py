from django.contrib import admin

from ProyectoWebServicios.models import Servicios

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido")
    readonly_fields = ("created", "updated")


admin.site.register(Servicios, AuthorAdmin)
