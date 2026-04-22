from django.urls import path 
from . import views

urlpatterns = [
 path ('pacientes/',views.dashboard_paciente, name='dashboard_paciente'),
 path('doctores/', views.dashboard_doctores, name='dashboard_doctores'), 
 path('gerencia/', views.dashboard_gerente, name='dashboard_gerente'),
 path('recepcion/', views.dashboard_recepcionista, name='dashboard_recepcionista'),

]
