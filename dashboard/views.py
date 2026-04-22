from django.http import HttpResponse
from .models import Paciente

# Create your views here.
def dashboard_pacientes (request):
    Paciente = Paciente.objects.all().order_by('-fecha_registro')
    total_pacientes = Paciente.count()

    context = {
        'pacientes':Paciente,
        'total_pacientes':total_pacientes,
    }
    return render (request , 'dashboard.html' , context)
