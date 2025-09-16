"""Tests para la clase Board."""

import unittest
from core.Board import Board
from core.Checker import Checker
from core.ColorFicha import ColorFicha

class TestBoard(unittest.TestCase):

    def setUp(self):
        """Configurar objetos antes de cada prueba."""
        self.tablero = Board()
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

    def test_setter_puntos_valido(self):
        nuevos_puntos = [[] for _ in range(24)]
        nuevos_puntos[0].append(self.ficha_blanca)
        self.tablero.puntos = nuevos_puntos
        self.assertEqual(len(self.tablero.puntos), 24)
        self.assertEqual(self.tablero.puntos[0][0].color, ColorFicha.BLANCA)
        self.assertEqual(len(self.tablero.puntos[0]), 1)
    
    def test_setter_puntos_lista_invalida_longitud(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.puntos = [[] for _ in range(23)]
        self.assertEqual(str(context.exception), "Los nuevos puntos deben ser una lista de 24 elementos.")
        
    def test_setter_puntos_no_es_lista(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.puntos = "no es una lista"
        self.assertEqual(str(context.exception), "Los nuevos puntos deben ser una lista de 24 elementos.")
        
    def test_setter_contenedor_blancas_valido(self):
        nuevo_contenedor = [self.ficha_blanca]
        self.tablero.contenedor_blancas = nuevo_contenedor
        self.assertEqual(self.tablero.contenedor_blancas, nuevo_contenedor)
    
    def test_setter_contenedor_negras_valido(self):
        nuevas_fichas = [self.ficha_negra]
        self.tablero.contenedor_negras = nuevas_fichas
        self.assertEqual(len(self.tablero.contenedor_negras), 1)
        self.assertEqual(self.tablero.contenedor_negras[0].color, ColorFicha.NEGRA)
        
        
    def test_resetear_tablero(self):
        self.tablero.agregar_ficha(0, self.ficha_blanca)
        self.tablero.agregar_ficha(5, self.ficha_negra)
        self.tablero.agregar_ficha_contenedor(self.ficha_blanca)
        self.tablero.agregar_ficha_contenedor(self.ficha_negra)
        #verifica que hayan fichas
        self.assertFalse(self.tablero.tablero_esta_vacio())
        self.assertFalse(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))
        self.assertFalse(self.tablero.contenedor_esta_vacio(ColorFicha.NEGRA))
        #resetea
        self.tablero.resetear_tablero()
        self.assertTrue(self.tablero.tablero_esta_vacio())
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.NEGRA))

    def test_limpiar_contenedores(self):
        self.tablero.agregar_ficha_contenedor(self.ficha_blanca)
        self.tablero.agregar_ficha_contenedor(self.ficha_negra)
        self.tablero.agregar_ficha_contenedor(Checker(ColorFicha.BLANCA))
        
        self.assertFalse(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))
        self.assertFalse(self.tablero.contenedor_esta_vacio(ColorFicha.NEGRA))
        self.tablero.limpiar_contenedores()
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.NEGRA))
        
    def test_iniciar_tablero_correcta_config(self):
        self.tablero.inicializar_tablero()

        self.assertEqual(self.tablero.contar_fichas(0), 2)
        self.assertEqual(self.tablero.contar_fichas(11), 5)
        self.assertEqual(self.tablero.contar_fichas(16), 3)
        self.assertEqual(self.tablero.contar_fichas(18), 5)
        
        self.assertEqual(self.tablero.contar_fichas(23), 2)
        self.assertEqual(self.tablero.contar_fichas(12), 5)
        self.assertEqual(self.tablero.contar_fichas(7), 3)
        self.assertEqual(self.tablero.contar_fichas(5), 5)
        

        for punto in [0, 11, 16, 18]:
            for ficha in self.tablero.obtener_fichas(punto):
                self.assertEqual(ficha.color, ColorFicha.NEGRA)
        
        for punto in [23, 12, 7, 5]:
            for ficha in self.tablero.obtener_fichas(punto):
                self.assertEqual(ficha.color, ColorFicha.BLANCA)
        
    def test_inicializar_tablero_colores_correctos(self):
        self.tablero.inicializar_tablero()
        
        # Verificar las fichas blancas
        self.assertEqual(self.tablero.contar_fichas(23), 2)
        self.assertEqual(self.tablero.contar_fichas(12), 5)
        self.assertEqual(self.tablero.contar_fichas(7), 3)
        self.assertEqual(self.tablero.contar_fichas(5), 5)
        
        for punto in [23, 12, 7, 5]:
            for ficha in self.tablero.obtener_fichas(punto):
                self.assertEqual(ficha.color, ColorFicha.BLANCA)
        
        # Verificar las fichas negras
        self.assertEqual(self.tablero.contar_fichas(0), 2)
        self.assertEqual(self.tablero.contar_fichas(11), 5)
        self.assertEqual(self.tablero.contar_fichas(16), 3)
        self.assertEqual(self.tablero.contar_fichas(18), 5)
        
        for punto in [0, 11, 16, 18]:
            for ficha in self.tablero.obtener_fichas(punto):
                self.assertEqual(ficha.color, ColorFicha.NEGRA)
    
    def test_inicializar_tablero_total_fichas(self):
        self.tablero.inicializar_tablero()
        total_fichas_blancas = sum(self.tablero.contar_fichas(punto) for punto in range(24) if self.tablero.obtener_color_punto(punto) == ColorFicha.BLANCA)
        total_fichas_negras = sum(self.tablero.contar_fichas(punto) for punto in range(24) if self.tablero.obtener_color_punto(punto) == ColorFicha.NEGRA)
        
        self.assertEqual(total_fichas_blancas, 15)
        self.assertEqual(total_fichas_negras, 15)
    
    def test_inicializar_tablero_puntos_vacios(self):
        self.tablero.inicializar_tablero()
        puntos_ocupados = {0, 5, 7, 11, 12, 16, 18, 23}
        for punto in range(24):
            if punto not in puntos_ocupados:
                self.assertTrue(self.tablero.punto_esta_vacio(punto))
    
    def test_limpiar_punto(self):
        self.tablero.agregar_ficha(4, self.ficha_blanca)
        self.tablero.agregar_ficha(4, self.ficha_negra)
        self.tablero.agregar_ficha(4, Checker(ColorFicha.BLANCA))
        
        fichas_removidas = self.tablero.limpiar_punto(4)
        self.assertEqual(len(fichas_removidas), 3)
        self.assertTrue(self.tablero.punto_esta_vacio(4))
        
        colores_removidos = [ficha.color for ficha in fichas_removidas]
        self.assertIn(ColorFicha.BLANCA, colores_removidos)
        self.assertIn(ColorFicha.NEGRA, colores_removidos)
        
    def test_inicializar_tablero_contenedores_vacios(self):
        self.tablero.inicializar_tablero()
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.NEGRA))

    def test_inicializar_tablero_limpia_estado_anterior(self):
        # Agregar fichas y contenedores antes de inicializar
        self.tablero.agregar_ficha(0, self.ficha_blanca)
        self.tablero.agregar_ficha(5, self.ficha_negra)
        self.tablero.agregar_ficha_contenedor(self.ficha_blanca)
        self.tablero.agregar_ficha_contenedor(self.ficha_negra)
        
        # Inicializar tablerito
        self.tablero.inicializar_tablero()
        
        # Verificar que se haya limpiado
        self.assertEqual(self.tablero.contar_fichas(0), 2)  
        self.assertEqual(self.tablero.contar_fichas(5), 5)  
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.BLANCA))
        self.assertTrue(self.tablero.contenedor_esta_vacio(ColorFicha.NEGRA))
        
    def test_inicializar_tablero_multiples_llamadas(self):
        self.tablero.inicializar_tablero()
        total_fichas_blancas_1 = sum(self.tablero.contar_fichas(punto) for punto in range(24) if self.tablero.obtener_color_punto(punto) == ColorFicha.BLANCA)
        total_fichas_negras_1 = sum(self.tablero.contar_fichas(punto) for punto in range(24) if self.tablero.obtener_color_punto(punto) == ColorFicha.NEGRA)
        
        self.assertEqual(total_fichas_blancas_1, 15)
        self.assertEqual(total_fichas_negras_1, 15)
        
        self.tablero.inicializar_tablero()
        total_fichas_blancas_2 = sum(self.tablero.contar_fichas(punto) for punto in range(24) if self.tablero.obtener_color_punto(punto) == ColorFicha.BLANCA)
        total_fichas_negras_2 = sum(self.tablero.contar_fichas(punto) for punto in range(24) if self.tablero.obtener_color_punto(punto) == ColorFicha.NEGRA)
        
        self.assertEqual(total_fichas_blancas_2, 15)
        self.assertEqual(total_fichas_negras_2, 15)
        

        self.assertEqual(total_fichas_blancas_1, total_fichas_blancas_2)
        self.assertEqual(total_fichas_negras_1, total_fichas_negras_2)    
        
    #Tests adicionales para coverage
    def test_contar_fichas_contenedor_color_invalido(self):
        self.assertEqual(self.tablero.contar_fichas_contenedor("no es un color"), 0)
        self.assertEqual(self.tablero.contar_fichas_contenedor(None), 0)
        
    def test_quitar_ficha_contenedor_vacio_ambos_colores(self):
        self.assertIsNone(self.tablero.quitar_ficha_contenedor(ColorFicha.BLANCA))
        self.assertIsNone(self.tablero.quitar_ficha_contenedor(ColorFicha.NEGRA))
        
    def test_obtener_color_punto_despues_de_quitar_ficha(self):
        self.tablero.agregar_ficha(10, self.ficha_blanca)
        color = self.tablero.obtener_color_punto(10)
        self.assertEqual(color, ColorFicha.BLANCA)
        
        self.tablero.quitar_ficha(10)
        color_despues = self.tablero.obtener_color_punto(10)
        self.assertIsNone(color_despues)
    
    def test_setter_puntos_tipo_incorrecto(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.puntos = "esto no es una lista"
        self.assertEqual(str(context.exception), "Los nuevos puntos deben ser una lista de 24 elementos.")
    
    def test_setter_contenedor_blancas_tipo_incorrecto(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.contenedor_blancas = "esto no es una lista"
        self.assertEqual(str(context.exception), "El nuevo contenedor debe ser una lista.")
        
    def test_setter_contenedor_negras_tipo_incorrecto(self):
        with self.assertRaises(ValueError) as context:
            self.tablero.contenedor_negras = 12345
        self.assertEqual(str(context.exception), "El nuevo contenedor debe ser una lista.")