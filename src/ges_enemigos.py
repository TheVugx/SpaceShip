import pygame
import random
from enemigo import EnemigoBase,EnemigoRectangular, EnemigoCircular, EnemigoCuadrado, EnemigoOctagonal, EnemigoHexagonal

class ges_enemigos():
    """
    Clase que se encargar de gestionar y crear Enemigos.\n
    Tipos de enemigos que maneja los siguientes enemigos:\n     
    cuadrado, rectangular, circular, hexagonal, octagonal
    """
    def __init__(self, lista_enemigos: str=[]):
        """
        Constructor de la clase ges_enemigos.
        :param lista_enemigos: lista de enemigos que el gameloop va a manejar
        """
        self.lista_enemigos = lista_enemigos

    def iniciar_enemigos(self, pantalla: pygame.Surface)->EnemigoBase:
        """
        Metodo que crea un enemigo al azar de la lista de enemigos anteriormente generada.\n
        :param pantalla: valores de la pantalla del juego.
        """
        self.tipo_enemigo = random.choice(self.lista_enemigos)

        if self.tipo_enemigo == "rectangular":
            nuevo_enemigo = EnemigoRectangular(pantalla, random.randrange(8,12,1), random.randrange(20,35,5), random.randrange(50,80,2))
        elif self.tipo_enemigo == "cuadrado":
            nuevo_enemigo = EnemigoCuadrado(pantalla, random.randrange(6,8,1), random.randrange(10,26,2))
        elif self.tipo_enemigo == "circular":
            nuevo_enemigo = EnemigoCircular(pantalla, random.randrange(4), random.randrange(20,40,2))
        elif self.tipo_enemigo == "hexagonal":
            nuevo_enemigo = EnemigoHexagonal(pantalla, random.randrange(4,6,1), random.randrange(40,60,2))
        elif self.tipo_enemigo == "octagonal":
            nuevo_enemigo = EnemigoOctagonal(pantalla, random.randrange(2,6,1), random.randrange(60,80,2))
        
        return nuevo_enemigo