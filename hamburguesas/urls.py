from django.urls import path
from . import views


urlpatterns = [
    # Catálogo público
    path('', views.catalogo_hamburguesas, name='catalogo_hamburguesas'),

    # Alias para evitar errores en templates viejos
    path('categorias/', views.lista_categorias_admin, name='lista_categorias'),

    # Gestión de hamburguesas
    path('gestion/', views.lista_hamburguesas_admin, name='lista_hamburguesas_admin'),
    path('gestion/crear/', views.crear_hamburguesa, name='crear_hamburguesa'),
    path('gestion/<int:pk>/editar/', views.editar_hamburguesa, name='editar_hamburguesa'),
    path('gestion/<int:pk>/eliminar/', views.eliminar_hamburguesa, name='eliminar_hamburguesa'),

    # Gestión de categorías
    path('gestion/categorias/', views.lista_categorias_admin, name='lista_categorias_admin'),
    path('gestion/categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('gestion/categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('gestion/categorias/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
]