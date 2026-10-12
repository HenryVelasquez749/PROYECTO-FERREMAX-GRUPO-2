# OWASP A05: Injection en campos SKU

## Prueba realizada

Se revisaron los usos de `sku` en reservas, ventas, mermas, traspasos,
órdenes, homologación POS y sincronización offline. Las consultas SQL de
`app.py` usan placeholders (`?`) y pasan el SKU como parámetro; no se
construyen consultas concatenando el valor recibido.

## Resultado

No se observó una ruta de inyección SQL directa en los campos SKU revisados.
La prueba de regresión debe conservar entradas adversariales como
`CEM-001' OR '1'='1` y verificar que no se transforma en una consulta válida.

## Recomendaciones

Mantener consultas parametrizadas, validar formato y longitud de SKU en el
borde de la API y añadir pruebas negativas para cada endpoint que lo reciba.
