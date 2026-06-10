from django import forms
from .models import Categoria, Hamburguesa


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Clásicas, Especiales, Mundialistas'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la categoría'
            }),
        }


class HamburguesaForm(forms.ModelForm):
    class Meta:
        model = Hamburguesa
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'categoria',
            'ingredientes',
            'imagen',
            'disponible',
        ]

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'categoria': 'Categoría',
            'ingredientes': 'Ingredientes',
            'imagen': 'Imagen',
            'disponible': 'Disponible',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Argentina Burger'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la hamburguesa'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 8500'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ingredientes': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }