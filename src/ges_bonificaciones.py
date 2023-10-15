import pygame
import random
from bonificacion import Bonificacion,Bonificacion_puntos, Bonificaciones_disparo

class ges_bonificaciones():
    """
    Clase que se encargar de gestionar y crear bonificaciones.
    """
    def __init__(self):
        """
        Constructor de la clase ges_bonificaciones.
        """
        pass
        
    def iniciar_bonificaciones(self, pantalla: pygame.Surface)->Bonificacion:
        """
        Metodo que crea una bonifiacion al azar de la lista["disparo", "chica", "mediana", "grande"].\n
        :param pantalla: valores de la pantalla del juego.
        """
        self.tipo_bonificacion = random.choice(["disparo", "chica", "mediana", "grande"]) 

        if self.tipo_bonificacion == "chica":
            nueva_bonificacion = Bonificacion_puntos(pantalla, random.randrange(8,12))
        elif self.tipo_bonificacion == "mediana":
            nueva_bonificacion = Bonificacion_puntos(pantalla, random.randrange(18,22))
        elif self.tipo_bonificacion == "grande":
            nueva_bonificacion = Bonificacion_puntos(pantalla, random.randrange(28,32))
        elif self.tipo_bonificacion == "disparo":
            nueva_bonificacion = Bonificaciones_disparo(pantalla)

        return nueva_bonificacion