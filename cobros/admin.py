from django.contrib import admin
from .models import cliente, vehiculo, espacio_estacionamiento, pago, tarifa, cobro

# Register your models here.
admin.site.register(cliente)
admin.site.register(vehiculo)
admin.site.register(espacio_estacionamiento)
admin.site.register(pago)
admin.site.register(tarifa)
admin.site.register(cobro)
