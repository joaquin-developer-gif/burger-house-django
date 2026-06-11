from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Hamburguesa, Categoria
from .forms import HamburguesaForm, CategoriaForm


# =========================================================
# HOME
# =========================================================

def home(request):
    hamburguesas_destacadas = Hamburguesa.objects.filter(disponible=True)[:3]

    return render(request, 'home.html', {
        'hamburguesas_destacadas': hamburguesas_destacadas
    })


# =========================================================
# CATÁLOGO PÚBLICO
# =========================================================

def catalogo_hamburguesas(request):
    hamburguesas = Hamburguesa.objects.filter(disponible=True).order_by('nombre')
    categorias = Categoria.objects.all().order_by('nombre')

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        hamburguesas = hamburguesas.filter(categoria_id=categoria_id)

    return render(request, 'hamburguesas/catalogo.html', {
        'hamburguesas': hamburguesas,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id
    })


# =========================================================
# GESTIÓN DE HAMBURGUESAS
# =========================================================

@login_required
@permission_required('hamburguesas.view_hamburguesa', raise_exception=True)
def lista_hamburguesas_admin(request):
    hamburguesas = Hamburguesa.objects.all().order_by('nombre')

    return render(request, 'hamburguesas/gestion/lista_hamburguesas_admin.html', {
        'hamburguesas': hamburguesas
    })


@login_required
@permission_required('hamburguesas.add_hamburguesa', raise_exception=True)
def crear_hamburguesa(request):
    if request.method == 'POST':
        form = HamburguesaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Hamburguesa creada correctamente.')
            return redirect('lista_hamburguesas_admin')
    else:
        form = HamburguesaForm()

    return render(request, 'hamburguesas/gestion/form_hamburguesa.html', {
        'form': form,
        'titulo': 'Crear hamburguesa',
        'boton': 'Guardar'
    })


@login_required
@permission_required('hamburguesas.change_hamburguesa', raise_exception=True)
def editar_hamburguesa(request, pk):
    hamburguesa = get_object_or_404(Hamburguesa, pk=pk)

    if request.method == 'POST':
        form = HamburguesaForm(request.POST, request.FILES, instance=hamburguesa)

        if form.is_valid():
            form.save()
            messages.success(request, 'Hamburguesa actualizada correctamente.')
            return redirect('lista_hamburguesas_admin')
    else:
        form = HamburguesaForm(instance=hamburguesa)

    return render(request, 'hamburguesas/gestion/form_hamburguesa.html', {
        'form': form,
        'titulo': 'Editar hamburguesa',
        'boton': 'Actualizar'
    })


@login_required
@permission_required('hamburguesas.delete_hamburguesa', raise_exception=True)
def eliminar_hamburguesa(request, pk):
    hamburguesa = get_object_or_404(Hamburguesa, pk=pk)

    if request.method == 'POST':
        hamburguesa.delete()
        messages.success(request, 'Hamburguesa eliminada correctamente.')
        return redirect('lista_hamburguesas_admin')

    return render(request, 'hamburguesas/gestion/confirmar_eliminar_hamburguesa.html', {
        'hamburguesa': hamburguesa
    })


# =========================================================
# GESTIÓN DE CATEGORÍAS
# =========================================================

@login_required
@permission_required('hamburguesas.view_categoria', raise_exception=True)
def lista_categorias_admin(request):
    categorias = Categoria.objects.all().order_by('nombre')

    return render(request, 'hamburguesas/gestion/lista_categorias_admin.html', {
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
            return redirect('lista_categorias_admin')
    else:
        form = CategoriaForm()

    return render(request, 'hamburguesas/gestion/form_categoria.html', {
        'form': form,
        'titulo': 'Crear categoría',
        'boton': 'Guardar'
    })


@login_required
@permission_required('hamburguesas.change_categoria', raise_exception=True)
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('lista_categorias_admin')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'hamburguesas/gestion/form_categoria.html', {
        'form': form,
        'titulo': 'Editar categoría',
        'boton': 'Actualizar'
    })


@login_required
@permission_required('hamburguesas.delete_categoria', raise_exception=True)
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('lista_categorias_admin')

    return render(request, 'hamburguesas/gestion/confirmar_eliminar_categoria.html', {
        'categoria': categoria
    })