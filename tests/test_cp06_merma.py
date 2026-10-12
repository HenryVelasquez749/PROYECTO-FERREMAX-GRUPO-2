from .base import FerremaxTestCase


class CP06MermaTest(FerremaxTestCase):
    def test_bodega_registra_merma_por_dano(self):
        response = self.client.post(
            "/api/merma",
            json={
                "sku": "FIER-02",
                "sucursal": "Maipú",
                "cantidad": 2,
                "motivo": "Daño durante traslado",
                "rol": "Bodega",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["success"])
        self.assertEqual(self.stock("FIER-02", "Maipú"), 43)
        audit = self.db.execute(
            "SELECT accion, detalles FROM bitacora_auditoria WHERE accion = 'AJUSTE_NEGATIVO_MERMA' ORDER BY id DESC LIMIT 1"
        ).fetchone()
        self.assertEqual(audit["accion"], "AJUSTE_NEGATIVO_MERMA")
        self.assertIn("Daño durante traslado", audit["detalles"])
