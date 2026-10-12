# OWASP A02: Cryptographic Failures y configuración TLS

## Hallazgo

La aplicación se inicia con el servidor de desarrollo de Flask en el puerto
5000 y no configura certificado, clave privada, `HTTPS` ni cabeceras de
transporte seguro. El despliegue local sirve como entorno de demostración,
pero no debe exponerse directamente a una red productiva.

## Impacto

Las credenciales futuras, roles y datos de operaciones podrían viajar sin
cifrado si el puerto se publica fuera del equipo local.

## Recomendación

Terminar TLS en un proxy o servidor WSGI configurado con TLS 1.2 o superior,
redireccionar HTTP a HTTPS, habilitar HSTS cuando el dominio esté listo y
mantener certificados fuera del repositorio.
