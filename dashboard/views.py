from django.http import HttpResponse
from .models import Paciente
from django.shortcuts import render
from .models import Recepcionista
from .models import Gerente
from .models import Doctor 

# Create your views here.
def dashboard_pacientes (request):
    Paciente = Paciente.objects.all().order_by('-fecha_registro')
    total_pacientes = Paciente.count()

    context = {
        'pacientes':Paciente,
        'total_pacientes':total_pacientes,
    }
    return render (request , 'dashboard.html' , context)



def dashboard_recepcionista(request):
    recepcionistas = Recepcionista.objects.all()
    context = {
        'recepcionistas': recepcionistas,
        'total_recepcion': recepcionistas.count(),
    }
    return render(request, 'dashboard_recepcionista.html', context)



def dashboard_gerente(request):
    gerentes = Gerente.objects.all()
    context = {
        'gerentes': gerentes,
    }
    return render(request, 'dashboard_gerente.html', context)


def dashboard_doctores(request):
    doctores = Doctor.objects.all()
    total_doctores = doctores.count()
    
    context = {
        'doctores': doctores,
        'total_doctores': total_doctores,
    }
    return render(request, 'dashboard_doctores.html', context)