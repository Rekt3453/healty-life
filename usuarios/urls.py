from django.urls import path
from .views import registro_paciente
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', registro_paciente, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', registro_paciente, name='registro'),
]