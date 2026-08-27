from django.shortcuts import render
from django.http import Http404
from .utils import obtener_zonas_con_resumen, obtener_zona_con_detalle


def listado_zonas(request):
    """Muestra todas las zonas registradas (CA-01, CA-02)."""
    zonas = obtener_zonas_con_resumen()
    contexto = {
        'zonas': zonas
    }
    return render(request, 'zonas/listado.html', contexto)


def detalle_zona(request, zona_id):
    """
    Muestra el detalle de una zona: dispositivos, consumo total y estado.
    Si la zona no existe, responde 404 (CA-08).
    """
    zona = obtener_zona_con_detalle(zona_id)
    if zona is None:
        raise Http404("La zona solicitada no existe.")

    contexto = {
        'zona': zona
    }
    return render(request, 'zonas/detalle.html', contexto)

