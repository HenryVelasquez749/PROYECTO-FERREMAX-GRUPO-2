# ISO/IEC 27000 A.9: Control de acceso

## Vinculación con el código

El control se refleja en las comprobaciones de rol antes de ejecutar acciones
privilegiadas:

- `app.py` restringe mermas y traspasos al rol `Bodega`.
- `app.py` restringe aprobación de órdenes y actualización de umbrales al rol
  `Admin`.
- `app.py` restringe la creación y cancelación de reservas a `Cajero` (con
  cancelación administrativa para `Admin`).
- `tests/test_cp10_rbac.py` verifica el rechazo HTTP 403 de una merma
  solicitada por un `Cajero`.

La implementación actual es una autorización basada en el valor de rol
recibido por la API. Para cumplir plenamente el control, debe enlazarse con
una identidad autenticada del servidor, como se detalla en el hallazgo OWASP
A01/A07.
