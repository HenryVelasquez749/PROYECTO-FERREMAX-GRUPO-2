# OWASP A01: Broken Access Control

## Alcance

Se revisaron las rutas de operaciones sensibles de `app.py`: reservas,
cancelaciones, mermas, traspasos, órdenes y actualización de umbrales.

## Hallazgo

Las rutas reciben el rol desde el cuerpo JSON (`rol`) y lo usan para autorizar
la operación. No existe una sesión autenticada ni una identidad firmada que
impida que un cliente cambie ese valor. La validación funciona como regla de
negocio en la interfaz actual, pero no constituye control de acceso fuerte
contra un consumidor externo.

## Evidencia y riesgo

- `POST /api/merma` exige `Bodega`.
- `POST /api/traspaso` exige `Bodega`.
- `POST /api/ordenes/aprobar/<id>` exige `Admin`.
- `POST /api/reservas/cancelar/<id>` acepta `Cajero` o `Admin`.

**Riesgo:** un atacante que pueda invocar la API directamente puede falsificar
el rol y ejecutar operaciones privilegiadas.

## Recomendación

Integrar autenticación de servidor (sesión o token), obtener el rol desde la
identidad autenticada y mantener estas comprobaciones como autorización
defensa-en-profundidad. El caso [CP-10](../../tests/test_cp10_rbac.py) cubre la
regla RBAC visible mientras se implementa esa capa.
