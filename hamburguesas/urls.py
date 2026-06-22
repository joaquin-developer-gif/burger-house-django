from django.urls import path
from . import views

app_name = "hamburguesas"

urlpatterns = [
    # Catálogo público
    path("", views.catalogo_hamburguesas, name="catalogo_hamburguesas"),

    # Pedidos
    path("<int:hamburguesa_id>/pedir/", views.pedir_hamburguesa, name="pedir_hamburguesa"),
    path("mis-pedidos/", views.mis_pedidos, name="mis_pedidos"),

    # Gestión de hamburguesas
    path("gestion/", views.lista_hamburguesas_admin, name="lista_hamburguesas_admin"),
    path("gestion/crear/", views.crear_hamburguesa, name="crear_hamburguesa"),
    path("gestion/editar/<int:pk>/", views.editar_hamburguesa, name="editar_hamburguesa"),
    path("gestion/eliminar/<int:pk>/", views.eliminar_hamburguesa, name="eliminar_hamburguesa"),

    # Gestión de categorías
    path("categorias/", views.lista_categorias_admin, name="lista_categorias_admin"),
    path("categorias/crear/", views.crear_categoria, name="crear_categoria"),
    path("categorias/editar/<int:pk>/", views.editar_categoria, name="editar_categoria"),
    path("categorias/eliminar/<int:pk>/", views.eliminar_categoria, name="eliminar_categoria"),
]