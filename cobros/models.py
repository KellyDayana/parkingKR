from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True, verbose_name="Identificación")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.identificacion}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Espacio(models.Model):
    numero = models.IntegerField(unique=True, choices=[(i, i) for i in range(1, 11)], verbose_name="Número")
    ocupado = models.BooleanField(default=False, verbose_name="Ocupado")

    def __str__(self):
        return f"Espacio {self.numero}"

    class Meta:
        verbose_name = "Espacio"
        verbose_name_plural = "Espacios"

class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE, verbose_name="Espacio")
    fecha_ingreso = models.DateTimeField(verbose_name="Fecha de Ingreso")
    fecha_salida = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Salida")
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Valor")

    def __str__(self):
        return f"Pago {self.id} - {self.cliente} - Espacio {self.espacio.numero}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"