from tests.base import FerremaxTestCase


class CP08DuplicadasTest(FerremaxTestCase):
    def test_detecta_y_bloquea_reservas_duplicadas_del_mismo_usuario(self):
        payload = {
            "sku": "PINT-01",
            "sucursal": "Maipú",
            "cliente": "Cliente CP-08",
            "cantidad": 1,
            "rol": "Cajero",
        }
        primera = self.client.post("/api/reservas", json=payload)
        segunda = self.client.post("/api/reservas", json=payload)

        self.assertEqual(primera.status_code, 200)
        self.assertEqual(segunda.status_code, 400)
        self.assertIn("Ya existe una reserva activa", segunda.json["message"])
        reservas = self.db.execute(
            "SELECT COUNT(*) AS total FROM reservas WHERE sku = 'PINT-01' AND cliente = 'Cliente CP-08' AND estado = 'ACTIVA'"
        ).fetchone()["total"]
        self.assertEqual(reservas, 1)
