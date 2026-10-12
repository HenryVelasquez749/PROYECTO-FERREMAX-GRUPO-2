import time

from .base import FerremaxTestCase


class CP09RendimientoTest(FerremaxTestCase):
    def test_sincronizacion_offline_completa_en_menos_de_5_segundos(self):
        operaciones = [
            {"sku": "CEM-001", "sucursal": "Maipú", "cantidad": 1},
            {"sku": "PINT-01", "sucursal": "Maipú", "cantidad": 1},
            {"sku": "FIER-02", "sucursal": "Maipú", "cantidad": 1},
        ]
        inicio = time.perf_counter()
        response = self.client.post("/api/sincronizar-offline", json=operaciones)
        duracion = time.perf_counter() - inicio

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["success"])
        self.assertLess(duracion, 5.0)
        self.assertIn("3 ventas", response.json["message"])
