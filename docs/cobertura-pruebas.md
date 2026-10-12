# Cobertura de funciones del prototipo

| Función | Endpoint o interfaz | Prueba asociada | Estado |
|---|---|---|---|
| Stock consolidado y alertas | `GET /api/stock-consolidado` | Consulta de SKU, total global y alerta bajo umbral | Asociada |
| Venta local | `POST /api/vender` | Venta autorizada, falta de stock y rol incorrecto | Asociada |
| Merma | `POST /api/merma` | Descuento con motivo y rechazo de rol | Asociada |
| Devolución | `POST /api/devolucion` | Reintegro de stock y SKU inexistente | Asociada |
| Homologación | `GET /api/pos-antiguo/homologar/<sku>` | SKU conocido y desconocido | Asociada |
| Traspaso FIFO | `POST /api/traspaso` | Saldo origen/destino y rol Bodega | Asociada |
| Compras | `GET/POST /api/ordenes` | Crear borrador, listar y aprobar | Asociada |
| Segregación | `POST /api/ordenes/aprobar/<id>` | Rechazo de aprobación no administrativa | Asociada |
| Umbrales | `POST /api/umbral/actualizar` | Actualización Admin y rechazo de otro rol | Asociada |
| Reservas | `GET/POST /api/reservas` | Crear reserva, duplicidad y falta de stock | Asociada |
| Liberación | `POST /api/reservas/cancelar/<id>` | Cancelación y devolución de unidades | Asociada |
| Expiración | `POST /api/reservas/expirar` | Reserva vencida y bitácora | Asociada |
| Offline | `POST /api/sincronizar-offline` | Cola local y sincronización diferencial | Asociada |
| Auditoría | `GET /api/auditoria` | Presencia de fecha, rol, acción y detalle | Asociada |

La revisión cubre todas las funciones de negocio visibles del prototipo. La ejecución automatizada de estas pruebas queda como actividad de validación del entorno de entrega.