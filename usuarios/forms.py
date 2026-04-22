from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroPacienteForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellido')
    email = forms.EmailField(label='Correo Electrónico')
    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )
    cedula = forms.CharField(max_length=20, label='Cédula de Identidad', required=True, widget=forms.TextInput(attrs={'placeholder': 'Ej: V-12345678'}))
    telefono = forms.CharField(max_length= 20, label= 'telefono')
    
    
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'fecha_nacimiento', 'cedula', 'telefono')
        
def save(self, commit=True):
    user = super().save(commit=False)
    user.rol = 'paciente'  
    user.is_staff = False
    user.is_superuser = False
    if commit:
        user.save()
    return user