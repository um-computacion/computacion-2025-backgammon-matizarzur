from core.ColorFicha import ColorFicha

class Checker:
    def __init__(self, color: ColorFicha):
        self.__color = color  
    
    @property
    def color(self):
        return self.__color
    