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
            'fields': ('dni', 'nombre', 'telefono', 'direccion')

        }),
    )
    search_fields = ['nombre','dni']
    list_display = ['nombre','telefono','dni']

class ProductoAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('foto', 'nombre', 'precio', 'stock')

        }),
    )
    list_display = ['foto','nombre','precio','stock']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Divisa)
admin.site.register(Direccion, DireccionAdmin)
