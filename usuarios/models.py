from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username