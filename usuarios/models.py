from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    
    ROLES = [
        ('paciente', 'Paciente'),
        ('asistente', 'Asistente'),
        ('doctor', 'Doctor'),
        ('gerente', 'Gerente'),
        ('admin', 'Super Admin'),
    ]
    
    # El campo rol debe estar alineado con la variable ROLES
    rol = models.CharField(max_length=20, choices=ROLES, default='paciente')

    def __str__(self):
        return f"{self.username} - {self.rol}"