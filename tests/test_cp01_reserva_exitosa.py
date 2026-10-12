from .base import FerremaxTestCase


class CP01ReservaExitosaTest(FerremaxTestCase):
    def test_reserva_exitosa_en_sucursal_con_stock(self):
        response = self.client.post(
            "/api/reservas",
            json={
                "sku": "CEM-001",
                "sucursal": "Maipú",
                "cliente": "Cliente CP-01",
                "cantidad": 2,
                "rol": "Cajero",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["success"])
        self.assertEqual(self.stock("CEM-001", "Maipú"), 10)
        self.assertIsNotNone(self.active_reservation("CEM-001", "Cliente CP-01"))
