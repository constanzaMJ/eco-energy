# Análisis — EcoEnergy Fase 1

## Relaciones y multiplicidades

- Una **Zona** contiene **0 o muchos Dispositivos** (1 : 0..*).
- Un **Dispositivo** pertenece a **una sola Zona** (relación mediante `zona_id`).
- Una **Categoría** clasifica **0 o muchos Dispositivos** (1 : 0..*).
- Un **Dispositivo** pertenece a **una sola Categoría** (relación mediante `categoria_id`).

Las relaciones no usan claves foráneas de base de datos: se resuelven en Python, 
comparando `zona_id` y `categoria_id` contra los `id` de `zonas.json` y `categorias.json`.

## Claves de conexión

| Archivo | Clave propia | Clave(s) que referencia a otros archivos |
|---|---|---|
| `zonas.json` | `id` | — |
| `categorias.json` | `id` | — |
| `dispositivos.json` | `id` | `zona_id` → `zonas.json.id`, `categoria_id` → `categorias.json.id` |

## Matriz Criterio de aceptación | Archivo/Componente | Prueba

| Criterio | Archivo/Componente | Prueba realizada |
|---|---|---|
| CA-01 | `views.py` (`listado_zonas`), `utils.py` (`obtener_zonas_con_resumen`) | Se verificó que `/zonas/` muestra las 3 zonas de `zonas.json`. |
| CA-02 | `listado.html` | Cada tarjeta muestra nombre, límite, cantidad de dispositivos y botón "Ver detalle". |
| CA-03 | `detalle.html`, `utils.py` (`obtener_zona_con_detalle`) | El detalle muestra dispositivos, categoría, consumo y estado de cada zona. |
| CA-04 | `utils.py` | Cantidades y estado se calculan en Python (`sum()`, comparación), no están escritas en el HTML. |
| CA-05 | `utils.py` (`estado = 'ALERTA' if ... else 'NORMAL'`) | Se probó con Zona Sur (190 > 150 → ALERTA) y Zona Norte (400 < 500 → NORMAL). |
| CA-06 | `dispositivos.json`, `utils.py` | Se agregaron dispositivos nuevos al JSON y aparecieron sin tocar `views.py` ni templates. |
| CA-07 | `detalle.html` (bloque `{% else %}`) | Se probó una zona sin dispositivos asociados: muestra "Esta zona no tiene dispositivos". |
| CA-08 | `views.py` (`raise Http404`) | Se probó `/zonas/99/` (id inexistente): Django respondió 404. |
| CA-09 | `base.html`, `listado.html`, `detalle.html` | Se agregaron más zonas/dispositivos y la navegación se mantuvo accesible. |
| CA-10 | `detalle.html` (`table-responsive`) | La tabla de dispositivos permite scroll horizontal sin desbordar la página. |
| CA-11 | `base.html` | Header, navegación y tarjetas usan clases Bootstrap consistentes (`navbar`, `card`, `badge`). |
| CA-12 | `detalle.html` (badges con texto "NORMAL"/"ALERTA" + color) | El estado se comunica con texto y color, no solo color. |
| CA-13 | Proyecto completo | `python manage.py check` se ejecutó sin errores. |

## Alcance respetado

No se implementaron Models, migraciones, ORM, CRUD, formularios, autenticación 
ni soft delete, conforme al alcance obligatorio del enunciado. Toda la lógica 
de datos se resuelve con estructuras Python (listas, diccionarios, comprensiones) 
sobre los archivos JSON.