import pygame
import random
import math
from musica import Musica
from jugador import Jugador


class EnemigoBase(pygame.sprite.Sprite):
    """
    Clase Padre de Enemigos.
    """
    def __init__(self, pantalla):
        """
        Constructor de la clase Enemigos.\n
        :param pantalla: valores de la pantalla del juego.
        """
        super().__init__()
        self.color = (255,255,255)
        self.pantalla = pantalla
        self.velocidad_y = int
        self.colisionada = False

    def num_y(self) ->int:
        """
        Metodo que devuelve un numero al azar negativo para posicionar un enemigo arriba de la pantalla.
        """
        return -(random.randrange(50, self.pantalla.get_height(), 10))

    def update(self, musica: Musica, jugador: Jugador, colisiones_balas):
        """
        Metodo para actualizar el objeto enemigo, este metodo tambien gestiona
        las coliciones con las balas.\n
        :param musica: Una instancia de Musica.
        :param jugador: Una instancia de Jugador.
        :param colisiones_balas: groupcollide de grupo de enemigos y el grupo de balas.
        """
        self.rect.y += self.velocidad_y
        if self.rect.y > self.pantalla.get_height():
            self.recolocar()
            self.colisionada = False
        if colisiones_balas:
            musica.play_boom()
            for enemigo in colisiones_balas:
                if not enemigo.colisionada:
                    self.height = enemigo.rect.height
                    self.width = enemigo.rect.width
                    enemigo.kill()
                    jugador.aumentar_puntaje(int((self.height+self.width)/3))
                    enemigo.colisionada = True

    def dibujar(self):
        """
        Metodo que dibujar a una enemigos.
        """
        self.pantalla.blit(self.imagen, self.rect)

    def recolocar(self):
        """
        Metodo que repociciona a un enemigo luego de salir de la pantalla.
        """
        self.rect.x = random.randint(0, self.pantalla.get_width() - self.rect.width)
        self.rect.y = self.num_y()
        self.velocidad_y += round(random.uniform(0.30, 0.50))

class EnemigoRectangular(EnemigoBase):
    """
    Esta es la clase EnemigoRectangular que crea un enemigo con forma rectangular.
    """
    def __init__(self, pantalla: pygame.Surface, velocidad_y: int, ancho: int, alto: int):
        """
        Constructor de la clase EnemigoCuadrado.\n
        :param pantalla: valores de la pantalla del juego.
        :param velocidad_y: valor numerico para definir la velocidad (esta aumenta posteriormente).
        :param ancho: valor numerico para definir el ancho de este enemigo.
        :param alto: valor numerico para definir el alto de este enemigo.
        """
        super().__init__(pantalla)
        self.velocidad_y = velocidad_y
        self.imagen = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        self.imagen.fill(self.color)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - ancho)
        self.rect.y = self.num_y()

class EnemigoCircular(EnemigoBase):
    """
    Esta es la clase EnemigoCircular que crea un enemigo con forma circular.
    """
    def __init__(self, pantalla: pygame.Surface, velocidad_y: int, radio: int):
        """
        Constructor de la clase EnemigoCuadrado.\n
        :param pantalla: valores de la pantalla del juego.
        :param velocidad_y: valor numerico para definir la velocidad (esta aumenta posteriormente).
        :param radio: valor numerico para definir el radio de este enemigo.
        """
        super().__init__(pantalla)
        self.velocidad_y = velocidad_y
        self.radio = radio
        self.imagen = pygame.Surface((2 * radio, 2 * radio), pygame.SRCALPHA)
        pygame.draw.circle(self.imagen, self.color, (self.radio, self.radio), self.radio)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - 2 * radio)
        self.rect.y = self.num_y()

class EnemigoCuadrado(EnemigoBase):
    """
    Esta es la clase EnemigoCuadrado que crea un enemigo con forma cuadrada.
    """
    def __init__(self, pantalla: pygame.Surface, velocidad_y: int, lado: int):
        """
        Constructor de la clase EnemigoCuadrado.\n
        :param pantalla: valores de la pantalla del juego.
        :param velocidad_y: valor numerico para definir la velocidad (esta aumenta posteriormente).
        :param lado: valor numerico para definir el tamaño de este enemigo.
        """
        super().__init__(pantalla)
        self.velocidad_y = velocidad_y
        self.lado = lado
        self.imagen = pygame.Surface((lado, lado), pygame.SRCALPHA)
        self.imagen.fill(self.color)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - lado)
        self.rect.y = self.num_y()

class EnemigoHexagonal(EnemigoBase):
    """
    Esta es la clase EnemigoHexagonal que crea un enemigo con forma hexagoal.
    """
    def __init__(self, pantalla: pygame.Surface, velocidad_y: int, lado: int):
        """
        Constructor de la clase EnemigoHexagonal.\n
        :param pantalla: valores de la pantalla del juego.
        :param velocidad_y: valor numerico para definir la velocidad (esta aumenta posteriormente).
        :param lado: valor numerico para definir el tamaño de este enemigo.
        """
        super().__init__(pantalla)
        self.velocidad_y = velocidad_y
        self.lado = lado
        self.imagen = pygame.Surface((self.lado, self.lado), pygame.SRCALPHA)
        lados = 6
        angulo = math.pi / 3
        vertices = []
        for i in range(lados):
            x = int(self.lado / 2 + (self.lado / 2) * math.cos(i * angulo))
            y = int(self.lado / 2 + (self.lado / 2) * math.sin(i * angulo))
            vertices.append((x, y))
        pygame.draw.polygon(self.imagen, self.color, vertices)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - self.lado)
        self.rect.y = self.num_y()

class EnemigoOctagonal(EnemigoBase):
    """
    Esta es la clase EnemigoOctagonal que crea un enemigo con forma octagonal.
    """
    def __init__(self, pantalla: pygame.Surface, velocidad_y: int, lado: int):
        """
        Constructor de la clase EnemigoOctagonal.\n
        :param pantalla: valores de la pantalla del juego.
        :param velocidad_y: valor numerico para definir la velocidad (esta aumenta posteriormente).
        :param lado: valor numerico para definir el tamaño de este enemigo.
        """
        super().__init__(pantalla)
        self.velocidad_y = velocidad_y
        self.lado = lado
        self.imagen = pygame.Surface((self.lado, self.lado), pygame.SRCALPHA)
        lados = 8
        angulo = math.pi / 4
        vertices = []
        for i in range(lados):
            x = int(self.lado / 2 + (self.lado / 2) * math.cos(i * angulo))
            y = int(self.lado / 2 + (self.lado / 2) * math.sin(i * angulo))
            vertices.append((x, y))
        pygame.draw.polygon(self.imagen, self.color, vertices)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, pantalla.get_width() - self.lado)
        self.rect.y = self.num_y()