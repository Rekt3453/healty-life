from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    
    ROLES = [
        ('paciente', 'Paciente'),
        ('recepcionista', 'Recepcionista'),
        ('doctor', 'Doctor'),
        ('gerente', 'Gerente'),
        ('admin', 'Super Admin'),
    ]
    
    cedula = models.CharField(max_length=15, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='paciente')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.username} - {self.rol}"