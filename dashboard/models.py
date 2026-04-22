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

class Recepcionista(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} "
    
class Gerente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, default="Gerente General")
    departamento = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"
    

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    mpps = models.CharField(max_length=20, verbose_name="Número de Colegiado")
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"    
