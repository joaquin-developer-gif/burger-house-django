from django.contrib import admin
from .models import (
    Categoria,
    Ingrediente,
    Hamburguesa,
    MetodoPago,
    Pedido,
    DetallePedido,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    search_fields = ("nombre", "descripcion")
    list_filter = ("activa",)
    ordering = ("nombre",)


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)


@admin.register(Hamburguesa)
class HamburguesaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "disponible", "fecha_creacion")
    search_fields = ("nombre", "descripcion")
    list_filter = ("categoria", "disponible")
    ordering = ("nombre",)
    filter_horizontal = ("ingredientes",)


@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "tipo_entrega", "estado", "metodo_pago", "total", "fecha")
    search_fields = ("usuario__username", "telefono_contacto", "direccion_entrega")
    list_filter = ("estado", "tipo_entrega", "metodo_pago", "fecha")
    ordering = ("-fecha",)
    inlines = [DetallePedidoInline]


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "hamburguesa", "cantidad", "precio_unitario")
    search_fields = ("hamburguesa__nombre", "pedido__usuario__username")