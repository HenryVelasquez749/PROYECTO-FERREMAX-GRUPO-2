# OWASP A07: Authentication Failures

## Evaluación

La interfaz permite seleccionar el rol con un control HTML y lo envía en cada
solicitud. La API no implementa autenticación, expiración de sesión, bloqueo
por intentos fallidos ni verificación de credenciales.

## Riesgo

El selector de roles es una ayuda de navegación, no una frontera de seguridad.
Un cliente puede enviar directamente `rol: "Admin"` o `rol: "Bodega"`. Esto
mantiene el riesgo de A07 y se relaciona con el hallazgo A01.

## Próximo control

Añadir inicio de sesión con credenciales almacenadas de forma segura, sesión
con expiración y middleware que derive el rol desde el usuario autenticado.
Conservar las comprobaciones por rol en las rutas como defensa adicional.
