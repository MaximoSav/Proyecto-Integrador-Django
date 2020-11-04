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
            'fields': ('nombre', 'telefono', 'direccion')

        }),
    )
    search_fields = ['nombre','telefono']
    list_display = ['nombre','telefono','direccion']


class ProductoAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('foto', 'nombre', 'precio', 'stock')

        }),
    )
    list_display = ['foto','nombre','precio','stock']

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('nombre',)
        }),
    )
    list_display = ['nombre']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Divisa)
admin.site.register(Direccion, DireccionAdmin)
