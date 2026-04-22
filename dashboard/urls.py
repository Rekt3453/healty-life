from django.urls import path 
from . import views

urlpatterns = [
 path ('pacientes/',views.dashboard_pacientes),
 path ('recepcion/', views.dashboard_recepcionista, name='dashboard_recepcionista'),
 path('gerencia/', views.dashboard_gerente, name='dashboard_gerente'),
 path('doctores/', views.dashboard_doctores, name='dashboard_doctores'),

 ]