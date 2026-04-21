# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol del Usuario', {'fields': ('rol',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'is_staff')

admin.site.register(Usuario, CustomUserAdmin)