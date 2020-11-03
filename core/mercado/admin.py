from django.contrib import admin
from .models import *
# Register your models here.

class ClienteInline(admin.TabularInline):
    model = Cliente

class DireccionAdmin(admin.ModelAdmin):
    list_display = ['barrio','calle', 'numero']
    inlines = [ClienteInline]

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('nombre', 'DNI', 'telefono', 'direccion')

        }),
    )

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Divisa)
admin.site.register(Direccion, DireccionAdmin)
