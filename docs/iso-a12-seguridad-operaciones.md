# ISO/IEC 27000 A.12: Seguridad en las operaciones

## Vinculación con la bitácora

`registrar_auditoria` centraliza el registro de operaciones relevantes en
`bitacora_auditoria`, incluyendo reservas, cancelaciones, mermas, devoluciones,
traspasos, órdenes y sincronización offline. La ruta
`GET /api/auditoria` expone los últimos 100 eventos para revisión operativa.

Los casos CP-03, CP-04, CP-06, CP-07 y CP-10 validan eventos o efectos
operativos asociados a esta bitácora. Para una implementación productiva se
requieren controles adicionales de acceso, retención, integridad y respaldo,
tal como se documenta en OWASP A09.
