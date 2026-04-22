from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_naciemiento = models.DateField()
    cedula = models.CharField(max_length=100, unique=True)
    telefono = models. CharField(max_length=20)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.nombre} {self.apellido}"


