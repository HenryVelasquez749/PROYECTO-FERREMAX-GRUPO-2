# PROYECTO-FERREMAX-GRUPO-2

Sistema web para la gestión de inventario distribuido de FerreMax, con operación multi-sucursal, control de stock y trazabilidad de eventos.

## Características principales

- Gestión de inventario consolidado entre sucursales (Maipú, Puente Alto y La Florida).
- Simulación de operación offline/online con sincronización posterior.
- Flujo de ventas, reservas, devoluciones, mermas y traspasos.
- Gestión de órdenes de compra y aprobación por rol.
- Auditoría de acciones y control de acceso por roles (RBAC).
- Implementación de patrones de diseño (Singleton y Strategy).

## Tecnologías

- Python 3
- Flask
- SQLite
- HTML + Tailwind CSS (interfaz)
- `unittest` (pruebas)

## Estructura del repositorio

- `/app.py`: aplicación principal (API, lógica de negocio e inicialización de base de datos).
- `/templates/index.html`: interfaz web.
- `/tests`: suite de pruebas funcionales.
- `/docs`: documentación de requerimientos, trazabilidad, auditoría y seguridad.

## Requisitos previos

- Python 3.10 o superior
- pip

## Instalación

1. Clona el repositorio.
2. Entra al directorio del proyecto.
3. (Opcional) Crea y activa un entorno virtual.
4. Instala Flask:

```bash
pip install flask
```

## Ejecución local

```bash
python app.py
```

La aplicación quedará disponible en:

- http://127.0.0.1:5000/

## Pruebas

Para ejecutar la suite de pruebas:

```bash
python -m unittest discover -s tests -v
```

## Base de datos

- La base SQLite usada por defecto es `ferremax_multisucursal.db`.
- Al iniciar la aplicación se ejecuta `init_db()`, que crea tablas y carga datos semilla para pruebas.

## Documentación adicional

Revisa la carpeta `/docs` para:

- Requerimientos funcionales y no funcionales.
- Historias de usuario.
- Matrices de trazabilidad.
- Evidencia de pruebas y controles de seguridad.

## Estado

Proyecto académico orientado a validar requerimientos RF/RNF en un escenario de inventario distribuido.
