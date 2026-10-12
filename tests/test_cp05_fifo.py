from tests.base import FerremaxTestCase


class CP05FifoTest(FerremaxTestCase):
    def test_reservas_concurrentes_respetan_orden_fifo_y_stock(self):
        self.db.execute(
            "UPDATE inventario_sucursales SET stock = 3 WHERE sku = 'TUB-010' AND sucursal = 'Maipú'"
        )
        self.db.commit()

        primera = self.client.post(
            "/api/reservas",
            json={"sku": "TUB-010", "sucursal": "Maipú", "cliente": "FIFO-01", "cantidad": 2, "rol": "Cajero"},
        )
        segunda = self.client.post(
            "/api/reservas",
            json={"sku": "TUB-010", "sucursal": "Maipú", "cliente": "FIFO-02", "cantidad": 2, "rol": "Cajero"},
        )

        self.assertEqual(primera.status_code, 200)
        self.assertEqual(segunda.status_code, 400)
        self.assertEqual(self.stock("TUB-010", "Maipú"), 1)
        self.assertIsNotNone(self.active_reservation("TUB-010", "FIFO-01"))
        self.assertIsNone(self.active_reservation("TUB-010", "FIFO-02"))
