from django.contrib import admin
from django.urls import path, include
from zonas import views as zonas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zonas/', include('zonas.urls')),
    # Requerimiento Fase 2 (seccion 3.1): ruta /resumen-zonas/ con nombre
    # de ruta utilizable mediante la etiqueta {% url %} de Django.
    path('resumen-zonas/', zonas_views.resumen_zonas, name='resumen_zonas'),
]