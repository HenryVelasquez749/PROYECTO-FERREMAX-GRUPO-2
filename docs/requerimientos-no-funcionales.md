# Matriz de requerimientos no funcionales

| ID | Atributo de calidad | Requerimiento verificable | Evidencia prevista | Prioridad |
|---|---|---|---|---|
| RNF-01 | Rendimiento | Las operaciones locales y la sincronizacion diferencial deben responder en menos de 5 segundos en condiciones normales. | Medicion de `/api/sincronizar-offline` y registro de latencia. | Must |
| RNF-02 | Seguridad | El sistema debe aplicar control de acceso basado en roles y rechazar operaciones fuera del rol autorizado. | Respuestas HTTP 403, pruebas por rol y bitacora. | Must |
| RNF-03 | Disponibilidad y tolerancia a fallos | El cajero debe poder continuar ventas locales sin conectividad y sincronizarlas al recuperar la red. | Cola offline del navegador y `/api/sincronizar-offline`. | Must |
| RNF-04 | Integridad | Los movimientos de stock deben conservar cantidades consistentes entre sucursal origen, destino y reservas. | Pruebas de transacciones antes y despues de cada movimiento. | Must |
| RNF-05 | Usabilidad | Las operaciones frecuentes deben estar disponibles desde una interfaz web en espanol, con formularios y feedback de resultado. | Evidencias de `templates/index.html`. | Should |
| RNF-06 | Auditabilidad | Las operaciones sensibles deben dejar fecha, rol, accion y detalle en la bitacora de auditoria. | Tabla `bitacora_auditoria` y endpoint `/api/auditoria`. | Must |
| RNF-07 | Mantenibilidad | La logica debe conservar separacion por rutas y explicitar los patrones Strategy, Singleton y Observer usados por el prototipo. | Estructura de `app.py` y comentarios de implementacion. | Should |

## Criterio de cumplimiento

Cada RNF se considera cubierto cuando existe una evidencia reproducible en el backend, la interfaz o una prueba documentada. Las mediciones de rendimiento deben ejecutarse en el mismo entorno de referencia y registrar fecha, carga y resultado.