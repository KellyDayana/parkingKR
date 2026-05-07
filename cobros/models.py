from django.db import models

# Create your models here.
class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class espacio_estacionamiento(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10, unique=True)
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return f"Espacio {self.numero} - {'Ocupado' if self.ocupado else 'Disponible'}"
class pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(vehiculo, on_delete=models.CASCADE)
    espacio_estacionamiento = models.ForeignKey(espacio_estacionamiento, on_delete=models.CASCADE)
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id_pago} - {self.cliente} - {self.vehiculo} - {self.espacio_estacionamiento}"