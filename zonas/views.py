from django.shortcuts import render
from django.http import Http404
from .utils import (
    obtener_zonas_con_resumen,
    obtener_zona_con_detalle,
    obtener_resumen_por_zona,
)

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
def resumen_zonas(request):
    """
    Vista "Resumen de consumo por zona" (Fase 2, seccion 3).

    Carga y relaciona zonas.json y dispositivos.json, ejecuta los conteos y
    sumas por zona, aplica la regla de estado (3.3) y arma el contexto con:
    - resumen_zonas: un registro agregado por cada zona.
    - totales: cantidad de zonas, cantidad de dispositivos y consumo total.

    Toda la logica de agregacion vive aca (y en utils.py); el template solo
    presenta los valores recibidos, sin recalcular nada.
    """
    resumen_zonas_lista, totales = obtener_resumen_por_zona()

    contexto = {
        'resumen_zonas': resumen_zonas_lista,
        'totales': totales,
    }
    return render(request, 'zonas/resumen.html', contexto)

