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
