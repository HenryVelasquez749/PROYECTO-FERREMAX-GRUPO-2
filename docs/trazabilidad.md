# Matriz de trazabilidad RF/RNF hacia código y prueba

| Requisito | Código relacionado | Prueba o evidencia |
|---|---|---|
| RF-01 | `GET /api/stock-consolidado` (`get_stock_consolidado`) | Consultar los seis SKU semilla y comprobar stocks por sucursal y total global. |
| RF-02 | `POST /api/reservas` (`gestionar_reservas`) | Crear reserva con stock disponible y comprobar descuento, estado `ACTIVA` y expiración. |
| RF-03 | `POST /api/reservas/cancelar/<id>` (`cancelar_reserva`) y `POST /api/reservas/expirar` (`expirar_reservas`) | Cancelar y expirar reservas vencidas; verificar cambio de estado y reintegro de unidades. |

La matriz se completa incrementalmente a medida que se audita cada requisito contra el backend.