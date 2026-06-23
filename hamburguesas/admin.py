from django.contrib import admin, messages

from .models import (
    Categoria,
    Ingrediente,
    Hamburguesa,
    MetodoPago,
    Pedido,
    DetallePedido,
)


# =========================================================
# CATEGORÍAS
# =========================================================

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'activa',
        'descripcion_corta',
    )

    list_filter = (
        'activa',
    )

    search_fields = (
        'nombre',
        'descripcion',
    )

    ordering = (
        'nombre',
    )

    def descripcion_corta(self, obj):
        if obj.descripcion:
            return obj.descripcion[:60]
        return '-'

    descripcion_corta.short_description = 'Descripción'


# =========================================================
# INGREDIENTES
# =========================================================

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'descripcion_corta',
    )

    search_fields = (
        'nombre',
        'descripcion',
    )

    ordering = (
        'nombre',
    )

    def descripcion_corta(self, obj):
        if obj.descripcion:
            return obj.descripcion[:60]
        return '-'

    descripcion_corta.short_description = 'Descripción'


# =========================================================
# HAMBURGUESAS
# =========================================================

@admin.register(Hamburguesa)
class HamburguesaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'precio',
        'disponible',
        'fecha_creacion',
    )

    list_filter = (
        'disponible',
        'categoria',
        'fecha_creacion',
    )

    search_fields = (
        'nombre',
        'descripcion',
        'categoria__nombre',
        'ingredientes__nombre',
    )

    ordering = (
        'nombre',
    )

    filter_horizontal = (
        'ingredientes',
    )

    date_hierarchy = 'fecha_creacion'


# =========================================================
# MÉTODOS DE PAGO
# =========================================================

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'activo',
    )

    list_filter = (
        'activo',
    )

    search_fields = (
        'nombre',
    )

    ordering = (
        'nombre',
    )


# =========================================================
# DETALLES DE PEDIDOS INLINE
# =========================================================

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

    fields = (
        'hamburguesa',
        'cantidad',
        'precio_unitario',
        'subtotal_detalle',
    )

    readonly_fields = (
        'subtotal_detalle',
    )

    autocomplete_fields = (
        'hamburguesa',
    )

    def subtotal_detalle(self, obj):
        if obj.pk:
            return obj.subtotal()
        return '-'

    subtotal_detalle.short_description = 'Subtotal'


# =========================================================
# PEDIDOS
# =========================================================

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'tipo_entrega',
        'estado',
        'metodo_pago',
        'telefono_contacto',
        'total',
        'fecha',
    )

    list_filter = (
        'estado',
        'tipo_entrega',
        'metodo_pago',
        'fecha',
    )

    search_fields = (
        'usuario__username',
        'usuario__email',
        'telefono_contacto',
        'direccion_entrega',
        'observaciones',
    )

    ordering = (
        '-fecha',
    )

    readonly_fields = (
        'fecha',
        'total',
    )

    date_hierarchy = 'fecha'

    inlines = [
        DetallePedidoInline,
    ]

    actions = (
        'marcar_como_preparando',
        'marcar_como_listo',
        'marcar_como_entregado',
        'marcar_como_cancelado',
    )

    fieldsets = (
        ('Cliente', {
            'fields': (
                'usuario',
                'telefono_contacto',
            )
        }),
        ('Entrega y pago', {
            'fields': (
                'tipo_entrega',
                'direccion_entrega',
                'metodo_pago',
            )
        }),
        ('Estado del pedido', {
            'fields': (
                'estado',
                'observaciones',
            )
        }),
        ('Totales y fecha', {
            'fields': (
                'total',
                'fecha',
            )
        }),
    )

    def marcar_como_preparando(self, request, queryset):
        cantidad = queryset.update(estado='preparando')
        self.message_user(
            request,
            f'{cantidad} pedido/s marcado/s como preparando.',
            messages.SUCCESS
        )

    marcar_como_preparando.short_description = 'Marcar como preparando'

    def marcar_como_listo(self, request, queryset):
        cantidad = queryset.update(estado='listo')
        self.message_user(
            request,
            f'{cantidad} pedido/s marcado/s como listo/s.',
            messages.SUCCESS
        )

    marcar_como_listo.short_description = 'Marcar como listo'

    def marcar_como_entregado(self, request, queryset):
        cantidad = queryset.update(estado='entregado')
        self.message_user(
            request,
            f'{cantidad} pedido/s marcado/s como entregado/s.',
            messages.SUCCESS
        )

    marcar_como_entregado.short_description = 'Marcar como entregado/completado'

    def marcar_como_cancelado(self, request, queryset):
        cantidad = queryset.update(estado='cancelado')
        self.message_user(
            request,
            f'{cantidad} pedido/s marcado/s como cancelado/s.',
            messages.SUCCESS
        )

    marcar_como_cancelado.short_description = 'Marcar como cancelado'


# =========================================================
# DETALLES DE PEDIDOS
# =========================================================

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = (
        'pedido',
        'hamburguesa',
        'cantidad',
        'precio_unitario',
        'subtotal_detalle',
    )

    list_filter = (
        'hamburguesa',
        'pedido__estado',
    )

    search_fields = (
        'pedido__usuario__username',
        'hamburguesa__nombre',
    )

    ordering = (
        '-pedido__fecha',
    )

    autocomplete_fields = (
        'pedido',
        'hamburguesa',
    )

    def subtotal_detalle(self, obj):
        return obj.subtotal()

    subtotal_detalle.short_description = 'Subtotal'