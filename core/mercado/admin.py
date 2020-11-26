from django.contrib import admin
from .models import *
# Register your models here.

class ClienteInline(admin.TabularInline):
    model = Cliente

class DireccionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('barrio', 'calle', 'numero')

        }),
    )

    list_display = ['barrio','calle', 'numero']
    inlines = [ClienteInline]

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('DNI', 'nombre', 'telefono', 'direccion')

        }),
    )
    search_fields = ['nombre','telefono']
    list_display = ['nombre','telefono','direccion']


class ProductoAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('foto', 'nombre', 'descripcion', 'precio', 'stock', 'categoria')

        }),
    )
    list_display = ['nombre', 'descripcion', 'precio', 'stock', 'categoria']

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('nombre',)
        }),
    )
    list_display = ['nombre']

admin.site.register(Cliente,)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Direccion,)
admin.site.register(Destacado)
