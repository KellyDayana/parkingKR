from django.contrib import admin
from .models import Cliente, Espacio, Pago

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'apellido', 'telefono')
    search_fields = ('identificacion', 'nombre', 'apellido')

@admin.register(Espacio)
class EspacioAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ocupado')
    list_filter = ('ocupado',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'espacio', 'fecha_ingreso', 'fecha_salida', 'valor')
    list_filter = ('fecha_ingreso', 'espacio')
