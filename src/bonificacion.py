import pygame
import random
from musica import Musica
from jugador import Jugador

class Bonificacion(pygame.sprite.Sprite):
    """
    Clase Padre de Bonificacion
    """
    def __init__(self, pantalla: pygame.Surface):
        """
        Constructor de la clase Bonificacion.\n
        :param pantalla: valores de la pantalla del juego.
        """
        super().__init__()
        self.color = (255,255,255)
        self.pantalla = pantalla
        self.velocidad = 2
        self.tiempo_parpadeo = 0
        self.intervalo_parpadeo = 20
        self.recolectada = False
        self.visible = True


    def update(self):
        """
        Metodo para actualizar el objeto bonificaciones, este metodo tambien gestiona
        las coliciones con el jugador, y el parpadeo de las bonificaciones.\n
        """
        self.rect.y += self.velocidad
        self.tiempo_parpadeo += 1
            
        if self.tiempo_parpadeo >= self.intervalo_parpadeo:
            self.visible = not self.visible
            self.tiempo_parpadeo = 0
        if self.rect.y > self.pantalla.get_height() + self.rect.height:
            self.kill()
        
    def dibujar(self):
        """
        Metodo que dibujar a una bonificacion.
        """
        if self.visible:
            self.pantalla.blit(self.image, self.rect)


class Bonificacion_puntos(Bonificacion):
    """
    Esta es la clase de Bonificacion_puntos, donde se crea un objeto que representa a una Bonificacion 
    que al colicionar te entrega una cantidad de puntos definida.
    """
    def __init__(self, pantalla: pygame.Surface, tamano: int):
        """
        Constructor de la clase Bonificacion.\n
        :param pantalla: valores de la pantalla del juego.
        :param tamano: valor numerico para definir el tamaño de esta bonificacion
        (el tamaño influye en el puntaje).
        """
        super().__init__(pantalla)
        self.puntos = tamano
        self.image = pygame.Surface((tamano, tamano), pygame.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - tamano)
        self.rect.y = -tamano


class Bonificaciones_disparo(Bonificacion):
    """
    Esta es la clase de Bonificaciones_disparo, donde se crea un objeto que representa a una Bonificacion 
    que al colicionar te entrega disparos al jugador.
    """
    def __init__(self, pantalla):
        """
        Constructor de la clase Bonificacion.\n
        :param pantalla: valores de la pantalla del juego.
        """
        super().__init__(pantalla)
        self.intervalo_parpadeo = 5
        self.tamano = 16
        self.puntos = 0
        self.image = pygame.Surface((self.tamano, self.tamano), pygame.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - self.tamano)
        self.rect.y = -self.tamano
