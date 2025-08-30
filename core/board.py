from core.Checker import Checker
from core.ColorFicha import ColorFicha
class Tablero:

    def __init__(self):

        self.__puntos = []
        for i in range(24):
            self.__puntos.append([])  
            
        self.__contenedor_blancas = [] 
        self.__contenedor_negras = []  

    @property
    def puntos(self):
        return self.__puntos

    @property
    def contenedor_blancas(self):
        return self.__contenedor_blancas

    @property
    def contenedor_negras(self):
        return self.__contenedor_negras

    def __es_punto_valido(self, punto):
        """Verificar si un punto está dentro del rango válido (0-23)."""
        return 0 <= punto < 24

    def agregar_ficha(self, punto, ficha):
        """Agregar una ficha a un punto específico."""
        if self.__es_punto_valido(punto):
            self.__puntos[punto].append(ficha)

    def obtener_fichas(self, punto):
        """Obtener todas las fichas de un punto."""
        if self.__es_punto_valido(punto):
            return self.__puntos[punto]
        return []

    def contar_fichas(self, punto):
        """Contar cuántas fichas hay en un punto."""
        if self.__es_punto_valido(punto):
            return len(self.__puntos[punto])
        return 0

    def quitar_ficha(self, punto):
        """Quitar la última ficha de un punto."""
        if self.__es_punto_valido(punto) and len(self.__puntos[punto]) > 0:
            return self.__puntos[punto].pop()
        return None

    def punto_esta_vacio(self, punto):
        """Verificar si un punto está vacío."""
        if self.__es_punto_valido(punto):
            return len(self.__puntos[punto]) == 0
        return True

    def obtener_color_punto(self, punto):
        """Obtener el color de las fichas en un punto (si tiene fichas)."""
        fichas = self.obtener_fichas(punto)
        if len(fichas) > 0:
            return fichas[0].color
        return None

    def agregar_ficha_contenedor(self, ficha):
        """Agregar una ficha al contenedor correspondiente según su color."""
        if ficha.color == ColorFicha.BLANCA:
            self.__contenedor_blancas.append(ficha)
        elif ficha.color == ColorFicha.NEGRA:
            self.__contenedor_negras.append(ficha)

    def quitar_ficha_contenedor(self, color):
        """Quitar una ficha del contenedor según el color."""
        if color == ColorFicha.BLANCA and len(self.__contenedor_blancas) > 0:
            return self.__contenedor_blancas.pop()
        elif color == ColorFicha.NEGRA and len(self.__contenedor_negras) > 0:
            return self.__contenedor_negras.pop()
        return None

    def contar_fichas_contenedor(self, color):
        """Contar cuántas fichas hay en el contenedor de un color."""
        if color == ColorFicha.BLANCA:
            return len(self.__contenedor_blancas)
        elif color == ColorFicha.NEGRA:
            return len(self.__contenedor_negras)
        return 0

    def contenedor_esta_vacio(self, color):
        """Verificar si el contenedor de un color está vacío."""
        return self.contar_fichas_contenedor(color) == 0

    def limpiar_punto(self, punto):
        """Quitar todas las fichas de un punto."""
        if self.__es_punto_valido(punto):
            fichas_removidas = self.__puntos[punto].copy()
            self.__puntos[punto].clear()
            return fichas_removidas
        return []

    def tablero_esta_vacio(self):
        """Verificar si el tablero está completamente vacío."""
        return all(len(punto) == 0 for punto in self.__puntos)