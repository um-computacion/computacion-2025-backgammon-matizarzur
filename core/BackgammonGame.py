from core.Board import Board
from core.Dice import Dice
from core.Checker import Checker
from core.ColorFicha import ColorFicha
import random

class BackgammonGame:
    
    def __init__(self):
        self.__board = Board()
        self.__dice = Dice()
        self.__jugador_actual = None  # Se determina con la primera tirada
        self.__estado_juego = "CONFIGURACION"  # CONFIGURACION, TIRADA_INICIAL, JUGANDO, TERMINADO
        self.__ganador = None
        self.__bar_blancas = []  # Fichas blancas en la barra (capturadas)
        self.__bar_negras = []   # Fichas negras en la barra (capturadas)
        self.__movimientos_restantes = 0
        self.__tirada_inicial_blancas = None
        self.__tirada_inicial_negras = None
        
    # Properties con getters y setters
    @property
    def board(self):
        return self.__board
    
    @board.setter
    def board(self, nuevo_board):
        if isinstance(nuevo_board, Board):
            self.__board = nuevo_board
        else:
            raise ValueError("El board debe ser una instancia de Board")
    
    @property
    def dice(self):
        return self.__dice
    
    @dice.setter
    def dice(self, nuevo_dice):
        if isinstance(nuevo_dice, Dice):
            self.__dice = nuevo_dice
        else:
            raise ValueError("El dice debe ser una instancia de Dice")
    
    @property
    def jugador_actual(self):
        return self.__jugador_actual
    
    @jugador_actual.setter
    def jugador_actual(self, nuevo_jugador):
        if nuevo_jugador is None or isinstance(nuevo_jugador, ColorFicha):
            self.__jugador_actual = nuevo_jugador
        else:
            raise ValueError("El jugador_actual debe ser None o una instancia de ColorFicha")
    
    @property
    def estado_juego(self):
        return self.__estado_juego
    
    @estado_juego.setter
    def estado_juego(self, nuevo_estado):
        estados_validos = ["CONFIGURACION", "TIRADA_INICIAL", "JUGANDO", "TERMINADO"]
        if nuevo_estado in estados_validos:
            self.__estado_juego = nuevo_estado
        else:
            raise ValueError(f"El estado debe ser uno de: {estados_validos}")
    
    @property
    def ganador(self):
        return self.__ganador
    
    @ganador.setter
    def ganador(self, nuevo_ganador):
        if nuevo_ganador is None or isinstance(nuevo_ganador, ColorFicha):
            self.__ganador = nuevo_ganador
        else:
            raise ValueError("El ganador debe ser None o una instancia de ColorFicha")
    
    @property
    def bar_blancas(self):
        return self.__bar_blancas
    
    @bar_blancas.setter
    def bar_blancas(self, nueva_bar):
        if isinstance(nueva_bar, list):
            self.__bar_blancas = nueva_bar
        else:
            raise ValueError("La bar_blancas debe ser una lista")
    
    @property
    def bar_negras(self):
        return self.__bar_negras
    
    @bar_negras.setter
    def bar_negras(self, nueva_bar):
        if isinstance(nueva_bar, list):
            self.__bar_negras = nueva_bar
        else:
            raise ValueError("La bar_negras debe ser una lista")
    
    @property
    def movimientos_restantes(self):
        return self.__movimientos_restantes
    
    @movimientos_restantes.setter
    def movimientos_restantes(self, movimientos):
        if isinstance(movimientos, int) and movimientos >= 0:
            self.__movimientos_restantes = movimientos
        else:
            raise ValueError("Los movimientos restantes deben ser un entero no negativo")
    
    @property
    def tirada_inicial_blancas(self):
        return self.__tirada_inicial_blancas
    
    @tirada_inicial_blancas.setter
    def tirada_inicial_blancas(self, nueva_tirada):
        if nueva_tirada is None or (isinstance(nueva_tirada, int) and 1 <= nueva_tirada <= 6):
            self.__tirada_inicial_blancas = nueva_tirada
        else:
            raise ValueError("La tirada_inicial_blancas debe ser None o un entero entre 1 y 6")
    
    @property
    def tirada_inicial_negras(self):
        return self.__tirada_inicial_negras
    
    @tirada_inicial_negras.setter
    def tirada_inicial_negras(self, nueva_tirada):
        if nueva_tirada is None or (isinstance(nueva_tirada, int) and 1 <= nueva_tirada <= 6):
            self.__tirada_inicial_negras = nueva_tirada
        else:
            raise ValueError("La tirada_inicial_negras debe ser None o un entero entre 1 y 6")
    
    # Metodos principales del juego
        # Configura el tablero con las fichas en posición inicial
    def configurar_tablero(self):
        pass
        # Regla: ubicar fichas en los puntos iniciales de backgammon

    # Lanza un dado para decidir quién empieza
    def lanzar_dado_individual(self):
        pass
        # Devuelve un número entre 1 y 6

    # Determina qué jugador comienza la partida
    def quien_empieza(self):
        pass
        # Reglas: cada jugador tira un dado, si empatan se repite
        # El que gana empieza con esa tirada

    # Lanza los dados en turno normal
    def lanzar_dados(self):
        pass
        # Regla: si es doble → se usan 4 movimientos en vez de 2

    # Verifica si un movimiento es válido
    def es_movimiento_valido(self, punto_origen, punto_destino):
        pass
        # Regla: depende de la tirada, barra, captura, bearing off

    # Mueve una ficha de un punto a otro
    def mover_ficha(self, punto_origen, punto_destino):
        pass
        # Idea: usar el dado correcto, validar movimiento
        # Regla futuro: if la ficha sale del tablero (bearing off)

    # Verifica si un jugador puede empezar a sacar fichas
    def puede_sacar_fichas(self, color):
        pass
        # Regla: todas las fichas en el home board, barra vacía

    # Comprueba si hay un ganador
    def hay_ganador(self):
        pass
        # Regla: gana cuando un jugador sacó sus 15 fichas
        # Aclaración: ver video reglas completas

    # Cambia el turno al otro jugador
    def cambiar_turno(self):
        pass
        # Idea: si movimientos_restantes == 0, cambio de jugador
        # Futuro: usar clase Jugador (0 = blancas, 1 = negras)

    # Obtiene todos los movimientos válidos posibles
    def obtener_movimientos_validos(self):
        pass
        # Idea: recorrer tablero y generar movimientos legales

    # Verifica si el jugador actual tiene algún movimiento válido
    def tiene_movimientos_validos(self):
        pass
        # Devuelve True/False según haya o no jugadas posibles

    # Reinicia todo para una nueva partida
    def iniciar_nueva_partida(self):
        pass
        # Resetear estado, tablero, dados, barras y tiradas iniciales

    # Devuelve un resumen del estado del juego
    def obtener_estado_juego_completo(self):
        pass
        # Info: jugador_actual, estado, ganador, última tirada, etc.