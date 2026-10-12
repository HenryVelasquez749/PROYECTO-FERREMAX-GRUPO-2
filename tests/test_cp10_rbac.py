from .base import FerremaxTestCase


class CP10RbacTest(FerremaxTestCase):
    def test_rol_no_autorizado_no_puede_registrar_merma(self):
        response = self.client.post(
            "/api/merma",
            json={
                "sku": "CEM-001",
                "sucursal": "Maipú",
                "cantidad": 1,
                "motivo": "Daño",
                "rol": "Cajero",
            },
        )

        self.assertEqual(response.status_code, 403)
        self.assertFalse(response.json["success"])
        self.assertEqual(self.stock("CEM-001", "Maipú"), 12)
        audit = self.db.execute(
            "SELECT accion FROM bitacora_auditoria WHERE accion = 'MERMA_RECHAZADA' ORDER BY id DESC LIMIT 1"
        ).fetchone()
        self.assertEqual(audit["accion"], "MERMA_RECHAZADA")
