from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_zonas, name='listado_zonas'),
    path('<int:zona_id>/', views.detalle_zona, name='detalle_zona'),
]
