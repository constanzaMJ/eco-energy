import json
import os
from jsonschema import validate, ValidationError

# Rutas a los archivos JSON
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'zonas', 'data')

ZONAS_PATH = os.path.join(DATA_DIR, 'zonas.json')
CATEGORIAS_PATH = os.path.join(DATA_DIR, 'categorias.json')
DISPOSITIVOS_PATH = os.path.join(DATA_DIR, 'dispositivos.json')

# Esquemas de validación (aseguran que cada JSON tenga las claves correctas)
ZONA_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "nombre", "limite_kwh"],
        "properties": {
            "id": {"type": "integer"},
            "nombre": {"type": "string"},
            "limite_kwh": {"type": "number"}
        }
    }
}

CATEGORIA_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "nombre", "descripcion"],
        "properties": {
            "id": {"type": "integer"},
            "nombre": {"type": "string"},
            "descripcion": {"type": "string"}
        }
    }
}

DISPOSITIVO_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "nombre", "consumo_kwh", "zona_id", "categoria_id"],
        "properties": {
            "id": {"type": "integer"},
            "nombre": {"type": "string"},
            "consumo_kwh": {"type": "number"},
            "zona_id": {"type": "integer"},
            "categoria_id": {"type": "integer"}
        }
    }
}


def _cargar_json(path, schema):
    """Lee un archivo JSON y valida su estructura contra un schema."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise ValueError(f"JSON invalido en {path}: {e.message}")
    return data


def cargar_zonas():
    """Devuelve la lista de zonas leidas desde zonas.json."""
    return _cargar_json(ZONAS_PATH, ZONA_SCHEMA)


def cargar_categorias():
    """Devuelve la lista de categorias leidas desde categorias.json."""
    return _cargar_json(CATEGORIAS_PATH, CATEGORIA_SCHEMA)


def cargar_dispositivos():
    """Devuelve la lista de dispositivos leidos desde dispositivos.json."""
    return _cargar_json(DISPOSITIVOS_PATH, DISPOSITIVO_SCHEMA)


def obtener_zonas_con_resumen():
    """
    Devuelve todas las zonas, cada una con su cantidad de dispositivos
    asociados. Se usa para el listado (CA-01, CA-02).
    """
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    resultado = []
    for zona in zonas:
        cantidad = sum(1 for d in dispositivos if d['zona_id'] == zona['id'])
        resultado.append({
            **zona,
            'cantidad_dispositivos': cantidad
        })
    return resultado


def obtener_zona_con_detalle(zona_id):
    """
    Busca una zona por id y arma su detalle: dispositivos con su categoria,
    consumo total y estado (NORMAL/ALERTA). Devuelve None si la zona no existe
    (para que la view responda 404 - CA-08).
    """
    zonas = cargar_zonas()
    categorias = cargar_categorias()
    dispositivos = cargar_dispositivos()

    zona = next((z for z in zonas if z['id'] == zona_id), None)
    if zona is None:
        return None

    # Diccionario para buscar categorias por id rapidamente
    categorias_por_id = {c['id']: c for c in categorias}

    dispositivos_zona = []
    consumo_total = 0
    for d in dispositivos:
        if d['zona_id'] == zona_id:
            categoria = categorias_por_id.get(d['categoria_id'])
            dispositivos_zona.append({
                **d,
                'categoria_nombre': categoria['nombre'] if categoria else 'Sin categoria'
            })
            consumo_total += d['consumo_kwh']

    estado = 'ALERTA' if consumo_total > zona['limite_kwh'] else 'NORMAL'

    return {
        **zona,
        'dispositivos': dispositivos_zona,
        'consumo_total': consumo_total,
        'estado': estado
    }