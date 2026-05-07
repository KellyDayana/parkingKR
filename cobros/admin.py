from django.contrib import admin
from .models import cliente, vehiculo, espacio_estacionamiento, pago, tarifa, cobro

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'identificacion')
        }),
        ('Contacto', {
            'fields': ('email', 'telefono')
        }),
    )
    list_display = ('nombre', 'apellido', 'identificacion', 'email', 'telefono')

class VehiculoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información del Vehículo', {
            'fields': ('marca', 'modelo', 'placa')
        }),
        ('Cliente Asociado', {
            'fields': ('cliente',)
        }),
    )
    list_display = ('marca', 'modelo', 'placa', 'cliente')

class EspacioEstacionamientoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información del Espacio', {
            'fields': ('numero', 'ocupado')
        }),
    )
    list_display = ('numero', 'ocupado')

class PagoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información del Pago', {
            'fields': ('cliente', 'vehiculo', 'espacio_estacionamiento', 'fecha_hora_entrada', 'fecha_hora_salida', 'monto')
        }),
    )
    list_display = ('id_pago', 'cliente', 'vehiculo', 'espacio_estacionamiento', 'fecha_hora_entrada', 'fecha_hora_salida', 'monto')

class TarifaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información de la Tarifa', {
            'fields': ('descripcion', 'precio_por_hora')
        }),
    )
    list_display = ('descripcion', 'precio_por_hora')

class CobroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información del Cobro', {
            'fields': ('pago', 'tarifa', 'monto_total')
        }),
    )
    list_display = ('id_cobro', 'pago', 'tarifa', 'monto_total')

admin.site.register(cliente, ClienteAdmin)
admin.site.register(vehiculo, VehiculoAdmin)
admin.site.register(espacio_estacionamiento, EspacioEstacionamientoAdmin)
admin.site.register(pago, PagoAdmin)
admin.site.register(tarifa, TarifaAdmin)
admin.site.register(cobro, CobroAdmin)
