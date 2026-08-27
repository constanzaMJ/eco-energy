# Registro de uso de IA — EcoEnergy Fase 1

## Herramienta utilizada

Claude (Anthropic), a través de la interfaz de chat.

## Prompts utilizados (resumen)

Seguí una guía paso a paso que le pedí a la IA, organizada en las mismas etapas del desarrollo:

- Estructura inicial: cómo crear el entorno virtual, iniciar el proyecto Django (`startproject config .`) y la app `zonas`, y cómo registrarla en `INSTALLED_APPS`.
- Archivos JSON: contenido de ejemplo para `zonas.json`, `categorias.json` y `dispositivos.json` cumpliendo las claves y mínimos del enunciado (3 zonas, 3 categorías, 8 dispositivos), y cómo dejar al menos una zona en estado ALERTA para poder probar CA-05.
- Capa de datos: estructura de `utils.py` con carga y validación de JSON usando `jsonschema`, y funciones para relacionar zonas, dispositivos y categorías (`obtener_zonas_con_resumen`, `obtener_zona_con_detalle`).
- Vistas y rutas: `views.py` y `urls.py` (de la app y del proyecto) que conectan `/zonas/` y `/zonas/<id>/` con esas funciones, incluyendo el manejo de 404 para CA-08.
- Templates: `base.html`, `listado.html` y `detalle.html` en Bootstrap, siguiendo los bocetos del enunciado (tarjetas de zona, tabla de dispositivos, estados NORMAL/ALERTA con texto + color).
- Errores puntuales: cómo activar el entorno virtual en PowerShell y cómo resolver un `AttributeError` que me apareció en `views.py`.
- Documentación: estructura para README.md, ANALISIS.md e IA.md acorde al punto 8 del enunciado.

## Partes utilizadas y cambios propios

- **Estructura del proyecto** (carpetas, `startproject`, `startapp`, `.gitignore`): la usé tal como la propuso la IA, adaptando los comandos a mi entorno Windows/PowerShell.
- **`utils.py`**: adopté la estructura completa que propuso la IA (esquemas de `jsonschema`, carga de los tres JSON, cálculo de `cantidad_dispositivos`, `consumo_total` y `estado`). No reescribí la lógica; mi aporte fue verificarla antes de conectarla a las vistas: la corrí en `python manage.py shell` y confirmé que `obtener_zona_con_detalle(3)` devolvía `consumo_total: 190`, `limite_kwh: 150` y `estado: 'ALERTA'`, y que `obtener_zona_con_detalle(99)` devolvía `None` (la base del 404 de CA-08).
- **`views.py` y `urls.py`**: los usé como base de la IA. Verifiqué que el manejo de 404 (`raise Http404`) correspondiera a lo que pide CA-08, probando `/zonas/99/` en el navegador.
- **Templates (`base.html`, `listado.html`, `detalle.html`)**: la IA propuso la estructura HTML y las clases Bootstrap; los usé prácticamente como se sugirieron. Verifiqué en el navegador que los tres estados (zonas con datos, zona vacía, id inexistente) se vieran bien y que la tabla de dispositivos usara `table-responsive`.
- **Datos (`zonas.json`, `categorias.json`, `dispositivos.json`)**: mantuve los valores de ejemplo. La única decisión propia sobre los datos fue ajustar el `limite_kwh` de "Zona Sur" de 200 a 150, para que su consumo real (190 kWh) quedara por encima del límite y así poder probar el estado ALERTA exigido por CA-05.

En general seguí de cerca la guía que me generó la IA en vez de escribir la lógica desde cero. Entiendo cómo funciona cada parte y puedo explicarla —carga y validación de JSON, cómo se relacionan zonas/dispositivos/categorías por `zona_id`/`categoria_id`, cómo se calcula el estado, y por qué la vista lanza 404— pero lo documento con honestidad: mi aporte principal fue integrar, adaptar a mi entorno y verificar cada etapa, más que modificar la lógica que propuso la IA.

## Verificación realizada

- Corrí `python manage.py check` después de cada etapa (estructura inicial, JSON, `utils.py`, vistas/rutas, templates) y no arrojó errores.
- Probé manualmente en `python manage.py shell` las funciones de `utils.py` antes de conectarlas a las vistas, confirmando los valores de consumo y estado de cada zona.
- Probé en el navegador las rutas `/zonas/`, `/zonas/1/`, `/zonas/3/` (ALERTA) y `/zonas/99/` (404).
- Agregué temporalmente un dispositivo nuevo en `dispositivos.json` con `zona_id: 1` y, sin reiniciar el servidor, confirmé que apareció automáticamente en `/zonas/1/` (prueba de CA-06).
- Puedo explicar el funcionamiento completo de `utils.py`, `views.py` y los templates: por qué se usa `jsonschema`, cómo se relacionan los tres archivos JSON por id, y cómo se calcula el estado NORMAL/ALERTA.