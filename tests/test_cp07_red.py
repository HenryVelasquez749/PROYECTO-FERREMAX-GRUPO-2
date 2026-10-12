from tests.base import FerremaxTestCase


class CP07RedTest(FerremaxTestCase):
    def test_reserva_no_se_crea_si_la_sincronizacion_offline_deja_stock_insuficiente(self):
        sync = self.client.post(
            "/api/sincronizar-offline",
            json=[{"sku": "HERR-05", "sucursal": "Maipú", "cantidad": 3}],
        )
        self.assertEqual(sync.status_code, 200)

        response = self.client.post(
            "/api/reservas",
            json={
                "sku": "HERR-05",
                "sucursal": "Maipú",
                "cliente": "Cliente CP-07",
                "cantidad": 1,
                "rol": "Cajero",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json["success"])
        self.assertIsNone(self.active_reservation("HERR-05", "Cliente CP-07"))
