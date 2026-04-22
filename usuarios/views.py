from django.shortcuts import render, redirect
from .forms import RegistroPacienteForm
from django.contrib import messages

def registro_paciente(request):
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso')
            return redirect('login')
    else: 
        form = RegistroPacienteForm()
        return render(request, 'usuarios/registro.html', {'form': form})
        
def home (request):
    return render(request, 'usuarios/home.html')