# EcoEnergy — Fase 1

Aplicación Django que permite consultar zonas de consumo energético de EcoEnergy 
y el detalle de los dispositivos instalados en cada una, usando archivos JSON 
como fuente de datos.

## Requisitos

- Python 3.11+ (probado con Python 3.14)
- pip

## Instalación

1. Clonar el repositorio:

- git clone  https://github.com/constanzaMJ/eco-energy

- cd eco-energy

2. Crear y activar el entorno virtual:
 - python -m venv venv
 
- venv\Scripts\Activate.ps1 # Windows PowerShell

- source venv/bin/activate # macOS/Linux


3. Instalar dependencias:

- pip install -r requirements.txt

## Ejecución
- python manage.py check
- python manage.py runserver

La aplicación queda disponible en `http://127.0.0.1:8000/`.

## Rutas funcionales

| Ruta | Descripción |
|---|---|
| `/zonas/` | Lista todas las zonas registradas, con límite y cantidad de dispositivos. |
| `/zonas/<id>/` | Muestra el detalle de una zona: dispositivos, categoría, consumo total y estado (NORMAL/ALERTA). Si el id no existe, responde 404. |

## Datos

Los datos de la aplicación viven en tres archivos JSON dentro de `zonas/data/`:

- `zonas.json` — id, nombre, limite_kwh
- `categorias.json` — id, nombre, descripcion
- `dispositivos.json` — id, nombre, consumo_kwh, zona_id, categoria_id

## Pruebas realizadas

- Listado de zonas muestra las 3 zonas con su cantidad de dispositivos.
- Detalle de zona muestra correctamente estado NORMAL (Zona Norte, Zona Centro) 
  y ALERTA (Zona Sur, con consumo 190 kWh > límite 150 kWh).
- Se probó una zona sin dispositivos: muestra el mensaje "Esta zona no tiene dispositivos".
- Se probó un id de zona inexistente (`/zonas/99/`): responde 404.
- Se agregaron dispositivos nuevos al JSON y la interfaz los reflejó sin modificar código.

## Dependencias externas

- `jsonschema`: valida la estructura de los archivos JSON antes de procesarlos.

-----
envio del trabajo a aii realizado
