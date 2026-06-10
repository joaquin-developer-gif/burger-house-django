from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CategoriaForm, HamburguesaForm


from .models import Hamburguesa, Categoria
from .forms import CategoriaForm


def home(request):
    return render(request, 'home.html')


def catalogo_hamburguesas(request):
    hamburguesas = Hamburguesa.objects.all().order_by('nombre')

    return render(request, 'hamburguesas/catalogo.html', {
        'hamburguesas': hamburguesas
    })


def detalle_hamburguesa(request, hamburguesa_id):
    hamburguesa = get_object_or_404(Hamburguesa, id=hamburguesa_id)

    return render(request, 'hamburguesas/detalle.html', {
        'hamburguesa': hamburguesa
    })


@login_required
@permission_required('hamburguesas.view_categoria', raise_exception=True)
def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('nombre')

    return render(request, 'hamburguesas/categorias/lista.html', {
        'categorias': categorias
    })


@login_required
@permission_required('hamburguesas.add_categoria', raise_exception=True)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'hamburguesas/categorias/form.html', {
        'form': form,
        'titulo': 'Crear categoría',
        'boton': 'Guardar categoría'
    })


@login_required
@permission_required('hamburguesas.change_categoria', raise_exception=True)
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'hamburguesas/categorias/form.html', {
        'form': form,
        'titulo': 'Editar categoría',
        'boton': 'Guardar cambios'
    })


@login_required
@permission_required('hamburguesas.delete_categoria', raise_exception=True)
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('lista_categorias')

    return render(request, 'hamburguesas/categorias/confirmar_eliminar.html', {
        'categoria': categoria
    })