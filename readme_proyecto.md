# 🍔 Burger House Django

Proyecto web desarrollado con **Django** para la gestión de una hamburguesería.
El sistema permite visualizar un catálogo de hamburguesas, registrar usuarios, iniciar sesión, realizar pedidos y administrar hamburguesas y categorías mediante vistas protegidas con permisos.

---

## Descripción del proyecto

**Burger House** es una aplicación web gastronómica orientada a pedidos de hamburguesas para retiro en local o delivery.

El proyecto fue desarrollado como trabajo académico utilizando el framework **Django**, aplicando conceptos fundamentales de desarrollo web backend, autenticación de usuarios, manejo de formularios, modelos relacionados, carga de imágenes, permisos y CRUD completo.

---

## Funcionalidades principales

- Página de inicio con información del sitio.
- Catálogo público de hamburguesas.
- Visualización de hamburguesas con imagen, descripción, categoría y precio.
- Registro de usuarios.
- Inicio y cierre de sesión.
- Usuario personalizado extendiendo `AbstractUser`.
- Realización de pedidos por usuarios autenticados.
- Selección de tipo de entrega: retiro o delivery.
- Gestión de pedidos del usuario.
- CRUD completo de hamburguesas.
- CRUD completo de categorías.
- Carga de imágenes mediante `ImageField`.
- Panel de administración de Django personalizado.
- Uso de permisos y grupos para proteger vistas.
- Navegación dinámica según usuario autenticado y permisos.
- Uso de Bootstrap para diseño responsive.
- Uso de archivos estáticos y media.

---

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Git
- GitHub

---

## Estructura general del proyecto

```text
burger-house-django/
│
├── burger_house/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── hamburguesas/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── context_processors.py
│
├── usuarios/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── hamburguesas/
│   └── usuarios/
│
├── static/
│   ├── css/
│   └── img/
│
├── media/
│
├── docs/
│   └── screenshots/
│
├── manage.py
└── readme_proyecto.md
```

---

## Modelos principales

El proyecto cuenta con varios modelos relacionados entre sí:

- **Usuario**: usuario personalizado basado en `AbstractUser`.
- **Categoria**: categorías de hamburguesas.
- **Ingrediente**: ingredientes disponibles.
- **Hamburguesa**: producto principal del sistema, con imagen, precio, categoría e ingredientes.
- **MetodoPago**: métodos de pago disponibles.
- **Pedido**: pedido realizado por un usuario.
- **DetallePedido**: detalle de cada hamburguesa solicitada en un pedido.

---

## Autenticación y permisos

El sistema incluye autenticación completa de usuarios:

- Registro de usuarios.
- Login.
- Logout.
- Vistas protegidas con `login_required`.
- Vistas administrativas protegidas con `permission_required`.
- Menú dinámico según los permisos del usuario.

Ejemplo de permisos aplicados:

- Crear hamburguesas.
- Editar hamburguesas.
- Eliminar hamburguesas.
- Ver gestión de hamburguesas.
- Administrar categorías.

---

## Capturas del proyecto

### Página principal

![Home](docs/screenshots/home.png)

---

### Catálogo de hamburguesas

![Catálogo](docs/screenshots/catalogo.png)

---

### Login de usuario

![Login](docs/screenshots/login.png)

---

### Registro de usuario

![Registro](docs/screenshots/registro.png)

---

### Mis pedidos

![Mis pedidos](docs/screenshots/mis-pedidos.png)

---

### Gestión de hamburguesas

![Gestión de hamburguesas](docs/screenshots/gestion-hamburguesas.png)

---

### Crear hamburguesa

![Crear hamburguesa](docs/screenshots/crear-hamburguesa.png)

---

### Gestión de categorías

![Gestión de categorías](docs/screenshots/gestion-categorias.png)

---

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/joaquin-developer-gif/burger-house-django.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd burger-house-django
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si el archivo `requirements.txt` no existe, se puede generar con:

```bash
pip freeze > requirements.txt
```

### 6. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear superusuario

```bash
python manage.py createsuperuser
```

### 8. Levantar el servidor local

```bash
python manage.py runserver
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000/
```

---

## Comandos útiles

Verificar el estado general del proyecto:

```bash
python manage.py check
```

Ejecutar servidor local:

```bash
python manage.py runserver
```

Crear migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear usuario administrador:

```bash
python manage.py createsuperuser
```

---

## 🗃️ Panel de administración

El proyecto utiliza el panel de administración de Django para gestionar datos internos.

Acceso:

```text
http://127.0.0.1:8000/admin/
```

Desde el admin se pueden administrar:

- Usuarios.
- Categorías.
- Ingredientes.
- Hamburguesas.
- Métodos de pago.
- Pedidos.
- Detalles de pedidos.

---

## 🌐 Rutas principales

| Ruta                           | Descripción                    |
| ------------------------------ | ------------------------------ |
| `/`                            | Página principal               |
| `/hamburguesas/`               | Catálogo de hamburguesas       |
| `/usuarios/registro/`          | Registro de usuario            |
| `/usuarios/login/`             | Inicio de sesión               |
| `/usuarios/logout/`            | Cierre de sesión               |
| `/hamburguesas/mis-pedidos/`   | Pedidos del usuario            |
| `/hamburguesas/gestion/`       | Gestión de hamburguesas        |
| `/hamburguesas/gestion/crear/` | Crear hamburguesa              |
| `/hamburguesas/categorias/`    | Gestión de categorías          |
| `/admin/`                      | Panel de administración Django |

---

## ✅ Requisitos académicos cumplidos

- Proyecto Django funcional.
- Uso de al menos dos aplicaciones.
- Múltiples modelos relacionados.
- Uso de `ImageField`.
- Usuario personalizado con `AbstractUser`.
- Registro, login y logout desde templates.
- CRUD completo de hamburguesas.
- CRUD completo de categorías.
- Vistas protegidas por login y permisos.
- Panel admin personalizado con filtros, búsqueda y ordenamiento.
- Uso de templates.
- Uso de archivos estáticos.
- Uso de archivos media.
- Diseño responsive con Bootstrap.
- Repositorio versionado con Git y GitHub.

---

## 👨‍💻 Autor

**Joaquin Rodriguez**
GitHub: [joaquin-developer-gif](https://github.com/joaquin-developer-gif)

---
