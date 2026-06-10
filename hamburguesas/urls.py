from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalogo_hamburguesas, name='catalogo_hamburguesas'),

    # CRUD Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),

    # CRUD Hamburguesas
    path('gestion/', views.lista_hamburguesas_admin, name='lista_hamburguesas_admin'),
    path('gestion/crear/', views.crear_hamburguesa, name='crear_hamburguesa'),
    path('gestion/editar/<int:hamburguesa_id>/', views.editar_hamburguesa, name='editar_hamburguesa'),
    path('gestion/eliminar/<int:hamburguesa_id>/', views.eliminar_hamburguesa, name='eliminar_hamburguesa'),

    # Detalle público
    path('<int:hamburguesa_id>/', views.detalle_hamburguesa, name='detalle_hamburguesa'),
]