import unittest
from core.board import Tablero
from core.checker import Checker
from core.color_ficha import ColorFicha

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()
        self.ficha_blanca = Checker(ColorFicha.BLANCA)
        self.ficha_negra = Checker(ColorFicha.NEGRA)

    def test_crear_tablero_vacio(self):
        self.assertEqual(len(self.tablero.puntos), 24)
        self.assertTrue(self.tablero.tablero_esta_vacio())

    def test_agregar_ficha_punto(self):
        self.tablero.agregar_ficha(0, self.ficha_blanca)
        self.assertEqual(self.tablero.contar_fichas(0), 1)
        self.assertFalse(self.tablero.tablero_esta_vacio())

    def test_obtener_fichas_punto(self):
        self.tablero.agregar_ficha(5, self.ficha_blanca)
        fichas = self.tablero.obtener_fichas(5)
        self.assertEqual(len(fichas), 1)
        self.assertEqual(fichas[0].color, ColorFicha.BLANCA)

    def test_contar_fichas_punto_vacio(self):
        self.assertEqual(self.tablero.contar_fichas(10), 0)

    def test_punto_esta_vacio(self):
        self.assertTrue(self.tablero.punto_esta_vacio(0))
        self.tablero.agregar_ficha(0, self.ficha_blanca)
        self.assertFalse(self.tablero.punto_esta_vacio(0))

    def test_quitar_ficha(self):
        self.tablero.agregar_ficha(3, self.ficha_negra)
        ficha_quitada = self.tablero.quitar_ficha(3)
        self.assertEqual(ficha_quitada.color, ColorFicha.NEGRA)
        self.assertEqual(self.tablero.contar_fichas(3), 0)

    def test_obtener_color_punto(self):
        self.tablero.agregar_ficha(7, self.ficha_blanca)
        color = self.tablero.obtener_color_punto(7)
        self.assertEqual(color, ColorFicha.BLANCA)

    def test_obtener_color_punto_vacio(self):
        self.assertIsNone(self.tablero.obtener_color_punto(5))

    def test_agregar_ficha_contenedor(self):
        self.tablero.agregar_ficha_contenedor(self.ficha_blanca)
        self.assertEqual(self.tablero.contar_fichas_contenedor(ColorFicha.BLANCA), 1)
        self.assertFalse(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))

    def test_quitar_ficha_contenedor(self):
        self.tablero.agregar_ficha_contenedor(self.ficha_negra)
        ficha_quitada = self.tablero.quitar_ficha_contenedor(ColorFicha.NEGRA)
        self.assertEqual(ficha_quitada.color, ColorFicha.NEGRA)
        self.assertEqual(self.tablero.contar_fichas_contenedor(ColorFicha.NEGRA), 0)

    def test_quitar_ficha_contenedor_vacio(self):
        result = self.tablero.quitar_ficha_contenedor(ColorFicha.NEGRA)
        self.assertIsNone(result)

    def test_contenedor_esta_vacio(self):
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))

    # Tests para casos de puntos fuera de rango
    def test_obtener_fichas_punto_invalido(self):
        self.assertEqual(self.tablero.obtener_fichas(30), [])
        self.assertEqual(self.tablero.obtener_fichas(-5), [])

    def test_contar_fichas_punto_invalido(self):
        self.assertEqual(self.tablero.contar_fichas(-5), 0)
        self.assertEqual(self.tablero.contar_fichas(25), 0)

    def test_quitar_ficha_punto_invalido(self):
        self.assertIsNone(self.tablero.quitar_ficha(-1))
        self.assertIsNone(self.tablero.quitar_ficha(24))
        self.assertIsNone(self.tablero.quitar_ficha(50))

    def test_punto_esta_vacio_invalido(self):
        self.assertTrue(self.tablero.punto_esta_vacio(99))
        self.assertTrue(self.tablero.punto_esta_vacio(-1))

    def test_agregar_ficha_punto_invalido(self):
        ficha = Checker(ColorFicha.BLANCA)
        self.tablero.agregar_ficha(-1, ficha)
        self.tablero.agregar_ficha(24, ficha)
        self.assertTrue(self.tablero.tablero_esta_vacio())