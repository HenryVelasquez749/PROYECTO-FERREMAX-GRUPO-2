# Matriz de trazabilidad RF/RNF hacia código y prueba

| Requisito | Código relacionado | Prueba o evidencia |
|---|---|---|
| RF-01 | `GET /api/stock-consolidado` (`get_stock_consolidado`) | Consultar los seis SKU semilla y comprobar stocks por sucursal y total global. |
| RF-02 | `POST /api/reservas` (`gestionar_reservas`) | Crear reserva con stock disponible y comprobar descuento, estado `ACTIVA` y expiración. |
| RF-03 | `POST /api/reservas/cancelar/<id>` (`cancelar_reserva`) y `POST /api/reservas/expirar` (`expirar_reservas`) | Cancelar y expirar reservas vencidas; verificar cambio de estado y reintegro de unidades. |
| RF-04 | `POST /api/vender` (`vender`) | Vender como Cajero con stock suficiente y comprobar descuento y auditoría `VENTA_LOCAL`. |
| RF-05 | `POST /api/merma` (`registrar_merma`) | Registrar merma como Bodega y comprobar descuento, motivo y auditoría `AJUSTE_NEGATIVO_MERMA`. |
| RF-06 | `POST /api/devolucion` (`registrar_devolucion`) | Procesar devolución autorizada y comprobar incremento de stock y auditoría `DEVOLUCION_RECIBIDA`. |
| RF-07 | `GET /api/stock-consolidado` (`EvaluadorUrgencia`, `EstrategiaLeadTimeLargo`, `EstrategiaTemporadaAlta`) | Sembrar stock bajo umbral y comprobar `alerta_activa`, detalle y nivel de urgencia. |
| RF-08 | Interfaz `toggleRed`, `sincronizarColaOffline` y `POST /api/sincronizar-offline` | Desconectar el simulador, encolar una venta y comprobar sincronización al volver online. |
| RNF-03 | Cola offline de `templates/index.html` y `sincronizar_offline` | Repetir la prueba offline y verificar que las transacciones pendientes llegan al backend. |
| RF-09 | `GET /api/pos-antiguo/homologar/<sku_antiguo>` (`homologar_pos_antiguo`) | Consultar `POS-CEM-OLD` y comprobar respuesta `CEM-001` y auditoría de homologación. |
| RF-10 | `GET/POST /api/ordenes` (`gestionar_ordenes`) y `POST /api/ordenes/aprobar/<id>` (`aprobar_orden`) | Crear borrador como Bodega y aprobarlo como Admin; comprobar estado, stock y precio +30%. |
| RF-11 | Validaciones de rol en `gestionar_ordenes` y `aprobar_orden` | Intentar crear como Admin y aprobar como Bodega; ambos intentos deben responder 403. |

La matriz se completa incrementalmente a medida que se audita cada requisito contra el backend.