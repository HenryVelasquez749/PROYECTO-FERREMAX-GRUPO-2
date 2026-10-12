# Matriz de trazabilidad

| Caso | Requisito funcional / no funcional | Ruta o componente | Evidencia |
|---|---|---|---|
| CP-01 | RF-02 Reserva de stock | `POST /api/reservas` | `test_cp01_reserva_exitosa.py` |
| CP-02 | RF-02 Validación de stock | `POST /api/reservas` | `test_cp02_stock_insuficiente.py` |
| CP-03 | RF-03 Liberación a 24 h | `POST /api/reservas/expirar` | `test_cp03_expiracion.py` |
| CP-04 | RF-03 Cancelación manual | `POST /api/reservas/cancelar/<id>` | `test_cp04_cancelacion.py` |
| CP-05 | RF-12 FIFO y concurrencia | `POST /api/reservas` | `test_cp05_fifo.py` |
| CP-06 | RF-05 Registro de mermas | `POST /api/merma` | `test_cp06_merma.py` |
| CP-07 | RNF-01 Operación offline | `POST /api/sincronizar-offline` | `test_cp07_red.py` |
| CP-08 | RF-02 Anti-duplicidad | `POST /api/reservas` | `test_cp08_duplicadas.py` |
| CP-09 | RNF-01 Sincronización menor a 5 s | `POST /api/sincronizar-offline` | `test_cp09_rendimiento.py` |
| CP-10 | RF-05/RF-12 Control RBAC | Validación de rol en API | `test_cp10_rbac.py` |

Los casos se ejecutan con `python -m unittest discover -s tests -p "test_*.py"`.
