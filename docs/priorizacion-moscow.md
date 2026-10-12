# Priorizacion MoSCoW del modulo critico

El modulo critico es el control de inventario multi-sucursal, porque una inconsistencia de stock afecta ventas, reservas, compras y traspasos.

| Categoria | Requisitos | Justificacion |
|---|---|---|
| Must have | RF-01, RF-02, RF-03, RF-04, RF-05, RF-06, RF-07, RF-08, RF-10, RF-11, RF-13, RNF-01, RNF-02, RNF-03, RNF-04, RNF-06 | Sin estas capacidades el prototipo no puede operar, proteger movimientos ni demostrar continuidad y auditoria. |
| Should have | RF-09, RF-12, RF-14, RNF-05, RNF-07 | Aportan integracion, eficiencia operativa, configurabilidad y mantenibilidad sin impedir el flujo minimo. |
| Could have | Reportes exportables y panel historico de indicadores | Mejoran el analisis, pero no son necesarios para ejecutar el modulo critico. |
| Won't have (en esta entrega) | Integracion real con ERP, pagos y proveedores externos | Quedan fuera del alcance del prototipo y requieren contratos e infraestructura externa. |

## Regla de decision

Un cambio que comprometa stock, reservas, permisos o auditoria no puede degradar un requisito Must have. Los requisitos Should y Could se planifican despues de estabilizar el flujo critico.