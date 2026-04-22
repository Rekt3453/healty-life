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


class Doctor (models.Model):
    nombre = models.CharField ( max_length=100)
    apellido = models.CharField (max_length=100)
    fecha_nacimiento = models.DateField ()
    cedula = models.CharField (max_length=100)
    telefono = models.CharField (max_length=20)
    especialidad = models.CharField(max_length=100)

    def __str__ (self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    

class Gerente (models.Model):
    nombre = models.CharField ( max_length=100)
    apellido = models.CharField (max_length=100)
    fecha_nacimiento = models.DateField ()
    cedula = models.CharField (max_length=100)
    telefono = models.CharField (max_length=20)
    cargo = models.CharField(max_length=100, default="Gerente General")

    def __str__ (self):
        return f"{self.nombre} {self.apellido}"    


class Recepcionista (models.Model):
    nombre = models.CharField ( max_length=100)
    apellido = models.CharField (max_length=100)
    fecha_nacimiento = models.DateField ()
    cedula = models.CharField (max_length=100)
    telefono = models.CharField (max_length=20) 

    def __str__(self):
        return f"{self.nombre} {self.pellido}"
