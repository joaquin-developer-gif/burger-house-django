from django import forms

from .models import Hamburguesa, Categoria, Pedido, MetodoPago


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

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Hamburguesa Argentina'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción de la hamburguesa'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 8500'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ingredientes': forms.CheckboxSelectMultiple(),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'categoria': 'Categoría',
            'ingredientes': 'Ingredientes',
            'imagen': 'Imagen',
            'disponible': 'Disponible',
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre',
            'descripcion',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Clásicas, Premium, Veggie'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción breve de la categoría'
            }),
        }

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }


class PedidoForm(forms.ModelForm):
    cantidad = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Cantidad',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'placeholder': 'Ej: 1'
        })
    )

    class Meta:
        model = Pedido
        fields = [
            'tipo_entrega',
            'direccion_entrega',
            'telefono_contacto',
            'metodo_pago',
            'observaciones',
        ]

        widgets = {
            'tipo_entrega': forms.Select(attrs={
                'class': 'form-select'
            }),
            'direccion_entrega': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Solo completar si elegís delivery'
            }),
            'telefono_contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3584196481'
            }),
            'metodo_pago': forms.Select(attrs={
                'class': 'form-select'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ej: Sin cebolla, más salsa, retirar a las 22 hs'
            }),
        }

        labels = {
            'tipo_entrega': 'Tipo de entrega',
            'direccion_entrega': 'Dirección de entrega',
            'telefono_contacto': 'Teléfono de contacto',
            'metodo_pago': 'Método de pago',
            'observaciones': 'Observaciones',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['metodo_pago'].queryset = MetodoPago.objects.filter(activo=True)
        self.fields['metodo_pago'].empty_label = 'Seleccioná un método de pago'

    def clean(self):
        cleaned_data = super().clean()

        tipo_entrega = cleaned_data.get('tipo_entrega')
        direccion_entrega = cleaned_data.get('direccion_entrega')

        if tipo_entrega == 'delivery' and not direccion_entrega:
            self.add_error(
                'direccion_entrega',
                'La dirección es obligatoria para pedidos con delivery.'
            )

        return cleaned_data