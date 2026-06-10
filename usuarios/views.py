from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from .forms import RegistroUsuarioForm


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Usuario registrado correctamente. Ya podés iniciar sesión.'
            )
            return redirect('login')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {
        'form': form
    })


class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'


def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('home')
