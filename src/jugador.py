import pygame
from disparo import Disparo
from musica import Musica

class Jugador(pygame.sprite.Sprite):
    """
    Esta es la clase de jugador, donde se crea un objeto que representa a un jugador, 
    esta clase tiene los metodos para mover y manejar a un jugador.
    """
    def __init__(self, pantalla: pygame.Surface):
        """
        Constructor de la clase Jugador.\n
        :param pantalla: valores de la pantalla del juego.
        """
        super().__init__()
        self.imagen = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.polygon(self.imagen, (255, 255, 255), [(0, 50), (25, 0), (50, 50)])
        self.rect = self.imagen.get_rect()
        self.rect.center = (pantalla.get_width() // 2, pantalla.get_height() - 50)
        self.pantalla = pantalla
        self.puntaje = 0
        self.disparo = 0

    def mover_izquierda(self):
        """
        Metodo de la Clase Jugador para moverse a la izquierda
        """
        if self.rect.left > 0:
            self.rect.x -= 5

    def mover_derecha(self):
        """
        Metodo de la Clase Jugador para moverse a la derecha
        """
        if self.rect.right < self.pantalla.get_width():
            self.rect.x += 5
    
    def disparar(self, musica: Musica) -> Disparo:
        """
        Metodo de la Clase Jugador para disparar.\n
        :param musica: Una instancia de la clase musica.
        :return: Una instancia de la clase Disparo.
        """
        if self.disparo >= 1:
            musica.play_disparo()
            self.disparo -= 1
            self.nuevo_disparo = Disparo(self.rect)
            return self.nuevo_disparo

    def update(self):
        pass

    def dibujar(self): 
        """
        Metodo que dibujar al Jugador.
        """
        self.pantalla.blit(self.imagen, self.rect)

    def aumentar_puntaje(self, puntos = 1):
        """
        Metodo para aumentar el puntaje del Jugador.\n
        :param puntos: cantidad de puntos que quieres aumentar.
        """
        self.puntaje += puntos
        
    def aumentar_disparo(self, disparos = 1):
        """
        Metodo para aumentar los disparos del Jugador.\n
        :param disparos: cantidad de disparos que quieres aumentar.
        """
        self.disparo += disparos

    def iniciar_puntaje(self, puntos = 0):
        """
        Metodo para iniciar/reiniciar el puntaje del Jugador.\n
        :param puntos: valor que quieres como inicio de puntajes.
        """
        self.puntaje = puntos

    def iniciar_disparo(self, disparos = 2):
        """
        Metodo para iniciar/reiniciar los disparos del Jugador.\n
        :param disparos: valor que quieres como inicio de disparos.
        """
        self.disparo = disparos

