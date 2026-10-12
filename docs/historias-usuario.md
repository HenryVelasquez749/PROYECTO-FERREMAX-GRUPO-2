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