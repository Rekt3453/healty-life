from django.shortcuts import render
from usuarios.models import Usuario  

def dashboard_paciente(request):
    
    pacientes = Usuario.objects.filter(rol='paciente').order_by('-date_joined')
    total_pacientes = pacientes.count()

    context = {
        'pacientes': pacientes,
        'total_pacientes': total_pacientes,
    }
    return render(request, 'dashboard_paciente.html', context)

def dashboard_doctores(request):
    
    doctores = Usuario.objects.filter(rol='doctor').order_by('-date_joined')
    total_doctores = doctores.count()
    
    context = {
        'doctores': doctores,
        'total_doctores': total_doctores,
    }
    return render(request, 'dashboard_doctores.html', context)

def dashboard_gerente(request):
    
    gerentes = Usuario.objects.filter(rol='gerente')
    
    context = {
        'gerentes': gerentes,
        'total_gerentes': gerentes.count(),
    }
    return render(request, 'dashboard_gerente.html', context)

def dashboard_recepcionista(request):
    # Filtramos por rol 'recepcionista'
    recepcionistas = Usuario.objects.filter(rol='recepcionista')
    
    context = {
        'recepcionistas': recepcionistas,
        'total_recepcion': recepcionistas.count(),
    }
    return render(request, 'dashboard_recepcionista.html', context)