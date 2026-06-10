from django.urls import path
from .views import registro, UsuarioLoginView, cerrar_sesion


urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]