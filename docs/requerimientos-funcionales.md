# Matriz de requerimientos funcionales

| ID | Requerimiento | Actor principal | Criterio de aceptación | Prioridad |
|---|---|---|---|---|
| RF-01 | Consultar el stock consolidado por SKU y sucursal, incluyendo precio, proveedor y stock total. | Administrador, Gerente, Bodega, Cajero | La consulta devuelve una fila por SKU con existencias de Maipu, Puente Alto y La Florida. | Must |
| RF-02 | Crear reservas de inventario para un cliente desde una sucursal. | Cajero | La reserva descuenta stock, queda activa y registra una expiracion a 24 horas. | Must |
| RF-03 | Liberar reservas canceladas o expiradas y reintegrar sus unidades al inventario. | Cajero, Administrador, Sistema | Una reserva liberada cambia de estado y devuelve exactamente su cantidad al stock. | Must |
| RF-04 | Registrar ventas locales en la sucursal seleccionada. | Cajero | Una venta valida rol y disponibilidad, descuenta unidades y registra auditoria. | Must |
| RF-05 | Registrar mermas por dano durante traslado o recepcion. | Bodega | Una merma autorizada descuenta unidades, exige motivo y deja evidencia auditable. | Must |
| RF-06 | Procesar devoluciones de clientes. | Cajero, Bodega | Una devolucion valida la sucursal y reintegra las unidades al inventario. | Must |
| RF-07 | Detectar stock bajo umbral y calcular el nivel de urgencia de la alerta. | Sistema, Administrador | La respuesta informa alerta activa, detalle por sucursal y nivel de urgencia. | Must |
| RF-08 | Permitir operar ventas locales y acumular transacciones cuando no hay red. | Cajero | El modo offline mantiene la operacion local y sincroniza la cola al recuperar conectividad. | Must |
| RF-09 | Homologar SKU provenientes del POS antiguo al catalogo vigente. | Sistema POS | Un SKU antiguo conocido devuelve su SKU homologado y registra la integracion. | Should |
| RF-10 | Crear, consultar y aprobar ordenes de compra para reponer inventario. | Bodega, Administrador | Bodega crea borradores y Administrador aprueba, recibe mercaderia y actualiza stock. | Must |
| RF-11 | Aplicar segregacion de funciones en el flujo de compras. | Bodega, Administrador | Bodega no puede aprobar y Administrador no puede crear borradores. | Must |
| RF-12 | Ejecutar traspasos de inventario entre sucursales siguiendo orden FIFO. | Bodega | El traspaso descuenta origen, suma destino y conserva el orden de salida definido. | Should |
| RF-13 | Controlar el acceso a operaciones mediante roles RBAC. | Todos los usuarios | Una operacion no autorizada responde 403 y registra el intento cuando corresponde. | Must |
| RF-14 | Configurar el umbral critico de stock por SKU y sucursal. | Administrador | Solo Administrador puede guardar el umbral y el nuevo valor afecta las alertas. | Should |

## Alcance

Los requisitos cubren el prototipo multi-sucursal de FerreMax: inventario, reservas, ventas, devoluciones, mermas, compras, traspasos, seguridad por roles, operacion offline y auditoria. Los criterios se verifican contra la API Flask y la interfaz web incluida en el repositorio.