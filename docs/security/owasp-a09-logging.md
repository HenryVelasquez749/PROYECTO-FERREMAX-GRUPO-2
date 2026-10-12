# OWASP A09: Security Logging and Monitoring Failures

## Evaluación

Las operaciones críticas llaman a `registrar_auditoria` y dejan fecha, rol,
acción y detalle en `bitacora_auditoria`. Se cubrieron reservas, cancelaciones,
mermas, traspasos, órdenes, devoluciones y sincronización offline.

## Brechas observadas

- `GET /api/auditoria` no exige autenticación ni autorización.
- La bitácora está en SQLite y no tiene controles de retención, integridad o
  envío a un repositorio separado.
- Algunos rechazos de validación no generan evento de auditoría.

## Recomendaciones

Restringir la consulta a `Admin`, registrar también errores de validación
críticos, agregar correlación de solicitud y exportar los eventos a un
almacenamiento protegido contra modificación.
