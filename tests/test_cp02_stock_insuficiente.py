from .base import FerremaxTestCase


class CP02StockInsuficienteTest(FerremaxTestCase):
    def test_reserva_rechazada_por_stock_insuficiente(self):
        response = self.client.post(
            "/api/reservas",
            json={
                "sku": "CEM-001",
                "sucursal": "Puente Alto",
                "cliente": "Cliente CP-02",
                "cantidad": 1,
                "rol": "Cajero",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json["success"])
        self.assertEqual(self.stock("CEM-001", "Puente Alto"), 0)
        self.assertIsNone(self.active_reservation("CEM-001", "Cliente CP-02"))
