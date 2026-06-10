from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'telefono',
            'direccion',
            'password1',
            'password2',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }