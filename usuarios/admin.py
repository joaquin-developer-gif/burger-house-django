from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ("username", "email", "telefono", "direccion", "is_staff", "is_active")
    search_fields = ("username", "email", "telefono")
    list_filter = ("is_staff", "is_active", "groups")