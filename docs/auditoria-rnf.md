# Auditoria de cobertura no funcional

## RNF-01: latencia

El backend expone una sincronizacion diferencial en `/api/sincronizar-offline` y devuelve una medicion informativa de 1.2 segundos. La evidencia debe validarse con una medicion externa repetible; el valor documentado queda dentro del objetivo menor a 5 segundos, pero no sustituye una prueba de carga.

## RNF-06: auditoria ISO

Las operaciones sensibles llaman a `registrar_auditoria`, que persiste fecha, rol, accion y detalle en `bitacora_auditoria`. El endpoint `/api/auditoria` permite consultar las ultimas 100 entradas. La cobertura es funcional para el prototipo; para una auditoria ISO formal faltan retencion, integridad criptografica y control de acceso al reporte.

## Resultado

RNF-01: cubierto con evidencia pendiente de medicion independiente. RNF-06: cubierto en alcance de prototipo, con controles ISO formales identificados como trabajo futuro.