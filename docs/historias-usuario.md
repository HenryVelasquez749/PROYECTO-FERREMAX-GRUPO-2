# Especificacion de historia de usuario: traslados FIFO

## HU-FIFO-01

**Como** encargado de Bodega, **quiero** trasladar unidades de una sucursal a otra siguiendo FIFO, **para** entregar primero el inventario que ingreso antes al flujo operativo.

### Criterios de aceptacion

- El rol distinto de Bodega recibe HTTP 403.
- El origen debe tener stock suficiente y el destino debe existir.
- El movimiento descuenta el origen, suma el destino y registra auditoria.
- La seleccion de existencias respeta el orden ascendente de `id`.
- Un error no deja un movimiento parcial.

### Implementacion y prueba

La implementacion se encuentra en `POST /api/traspaso`, funcion `solicitar_traspaso`. La prueba usa un SKU con stock en Maipu, solicita unidades hacia Puente Alto y compara ambos saldos antes y despues.

# Especificacion: expiracion de reservas a 24 horas

## HU-RES-01

**Como** sistema de reservas, **quiero** liberar automaticamente una reserva activa al cumplir 24 horas, **para** devolver sus unidades al stock disponible sin intervencion manual.

### Reglas

- Al crear una reserva se calcula `fecha_expiracion` como fecha actual mas 24 horas.
- El proceso solo toma reservas `ACTIVA` cuya fecha ya vencio.
- Cada reserva pasa a `EXPIRADA` y reintegra exactamente su cantidad.
- La accion queda registrada como `RESERVA_EXPIRADA_AUTOMATICA`.

### Implementacion y prueba

La implementacion corresponde a `POST /api/reservas/expirar`, funcion `expirar_reservas`. La prueba prepara una reserva vencida, ejecuta el endpoint y verifica estado, stock liberado, cantidad procesada y bitacora.