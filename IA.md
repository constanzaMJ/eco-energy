# Registro de uso de IA — EcoEnergy Fase 1

## Herramienta utilizada

Claude (Anthropic), a través de la interfaz de chat.

## Prompts utilizados (resumen)

- Solicité una guía paso a paso para estructurar un proyecto Django que 
  cumpliera el enunciado de EcoEnergy (listado y detalle de zonas desde JSON).
- Pedí ejemplos de estructura para `utils.py` con carga y validación de JSON 
  usando `jsonschema`, y relación entre zonas, dispositivos y categorías.
- Pedí ejemplos de `views.py`, `urls.py` y templates Bootstrap siguiendo los 
  bocetos y criterios de aceptación del enunciado.
- Consulté cómo resolver errores puntuales (activación de entorno virtual en 
  PowerShell, error de `AttributeError` en `views.py`).

## Partes utilizadas y cambios propios

- **Estructura del proyecto** (carpetas, `startproject`, `startapp`): usada 
  como fue sugerida, adaptando nombres de carpetas a mi entorno Windows.
- **`utils.py`**: partí de la estructura sugerida por la IA (funciones de 
  carga, validación con `jsonschema`, cálculo de consumo y estado). 
  [Aquí debes anotar tú qué modificaste: por ejemplo, si cambiaste algún 
  nombre de función, agregaste manejo de errores adicional, cambiaste la 
  lógica de alguna validación, etc.]
- **`views.py` y `urls.py`**: usados como base, adaptando el manejo de 404 
  según lo que exige CA-08.
- **Templates (`base.html`, `listado.html`, `detalle.html`)**: la IA propuso 
  la estructura HTML y clases Bootstrap; yo ajusté [anota aquí qué cambiaste: 
  colores, textos, disposición de tarjetas, etc., si hiciste cambios].
- **Datos de `zonas.json`, `categorias.json`, `dispositivos.json`**: los 
  valores (nombres de zonas, dispositivos, consumos) fueron propuestos como 
  ejemplo; yo los revisé y decidí mantenerlos / los cambié por [completa].

## Verificación realizada

- Corrí `python manage.py check` después de cada cambio estructural.
- Probé manualmente en `python manage.py shell` las funciones de `utils.py` 
  antes de conectarlas a las vistas, confirmando que `obtener_zona_con_detalle(3)` 
  devuelve estado ALERTA correctamente.
- Probé en el navegador las rutas `/zonas/` y `/zonas/3/`, y el caso de error 
  `/zonas/99/`.
- Puedo explicar el funcionamiento completo de `utils.py`, `views.py` y los 
  templates, incluyendo por qué se usa `jsonschema` y cómo se calcula el estado.