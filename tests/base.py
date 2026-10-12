import unittest

from app import ConexionBaseDatos, app, init_db


class FerremaxTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        init_db()
        self.db = ConexionBaseDatos().conexion

    def stock(self, sku, sucursal):
        row = self.db.execute(
            "SELECT stock FROM inventario_sucursales WHERE sku = ? AND sucursal = ?",
            (sku, sucursal),
        ).fetchone()
        return row["stock"]

    def active_reservation(self, sku, cliente):
        return self.db.execute(
            "SELECT * FROM reservas WHERE sku = ? AND cliente = ? AND estado = 'ACTIVA'",
            (sku, cliente),
        ).fetchone()
