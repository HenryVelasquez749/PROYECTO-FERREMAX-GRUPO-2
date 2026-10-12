from datetime import datetime, timedelta

from .base import FerremaxTestCase


class CP03ExpiracionTest(FerremaxTestCase):
    def test_expiracion_automatica_devuelve_stock_a_las_24_horas(self):
        response = self.client.post(
            "/api/reservas",
            json={
                "sku": "PINT-01",
                "sucursal": "Maipú",
                "cliente": "Cliente CP-03",
                "cantidad": 2,
                "rol": "Cajero",
            },
        )
        self.assertEqual(response.status_code, 200)
        reserva = self.active_reservation("PINT-01", "Cliente CP-03")
        self.db.execute(
            "UPDATE reservas SET fecha_expiracion = ? WHERE id = ?",
            ((datetime.now() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"), reserva["id"]),
        )
        self.db.commit()

        response = self.client.post("/api/reservas/expirar")

        self.assertEqual(response.status_code, 200)
        self.assertIn("1 reservas", response.json["message"])
        self.assertEqual(self.stock("PINT-01", "Maipú"), 5)
        estado = self.db.execute(
            "SELECT estado FROM reservas WHERE id = ?", (reserva["id"],)
        ).fetchone()["estado"]
        self.assertEqual(estado, "EXPIRADA")
