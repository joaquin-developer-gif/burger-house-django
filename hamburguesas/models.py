
from django.conf import settings
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Hamburguesa(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="hamburguesas"
    )
    ingredientes = models.ManyToManyField(
        Ingrediente,
        blank=True,
        related_name="hamburguesas"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="hamburguesas/", blank=True, null=True)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hamburguesa"
        verbose_name_plural = "Hamburguesas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Método de pago"
        verbose_name_plural = "Métodos de pago"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    TIPO_ENTREGA = [
        ("retiro", "Retiro en el local"),
        ("delivery", "Delivery a domicilio"),
    ]

    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("preparando", "Preparando"),
        ("listo", "Listo"),
        ("en_camino", "En camino"),
        ("entregado", "Entregado"),
        ("cancelado", "Cancelado"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pedidos"
    )
    metodo_pago = models.ForeignKey(
        MetodoPago,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pedidos"
    )
    tipo_entrega = models.CharField(max_length=20, choices=TIPO_ENTREGA)
    direccion_entrega = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    observaciones = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-fecha"]

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

    def calcular_total(self):
        total = sum(detalle.subtotal() for detalle in self.detalles.all())
        return total

    def actualizar_total(self):
        self.total = self.calcular_total()
        self.save()


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    hamburguesa = models.ForeignKey(
        Hamburguesa,
        on_delete=models.CASCADE,
        related_name="detalles_pedido"
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Detalle de pedido"
        verbose_name_plural = "Detalles de pedidos"

    def __str__(self):
        return f"{self.cantidad} x {self.hamburguesa.nombre}"

    def subtotal(self):
        return self.cantidad * self.precio_unitario
