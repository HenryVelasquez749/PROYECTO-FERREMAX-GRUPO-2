from tests.base import FerremaxTestCase


class CP04CancelacionTest(FerremaxTestCase):
    def test_cajero_cancela_reserva_y_recupera_stock(self):
        self.client.post(
            "/api/reservas",
            json={
                "sku": "FIER-02",
                "sucursal": "Maipú",
                "cliente": "Cliente CP-04",
                "cantidad": 3,
                "rol": "Cajero",
            },
        )
        reserva = self.active_reservation("FIER-02", "Cliente CP-04")

        response = self.client.post(
            f"/api/reservas/cancelar/{reserva['id']}",
            json={"rol": "Cajero"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["success"])
        self.assertEqual(self.stock("FIER-02", "Maipú"), 45)
        estado = self.db.execute(
            "SELECT estado FROM reservas WHERE id = ?", (reserva["id"],)
        ).fetchone()["estado"]
        self.assertEqual(estado, "CANCELADA")
