from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hamburguesas.views import home


urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', home, name='home'),

    # App hamburguesas
    path('hamburguesas/', include('hamburguesas.urls')),

    path('usuarios/', include('usuarios.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)