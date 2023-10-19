import pygame

class Disparo(pygame.sprite.Sprite):
    """
    clase Disparo.
    """
    def __init__(self, jugador_rect: pygame.Rect, pantalla: pygame.Surface):
        """
        constructor de la clase Disparo.\n
        :param jugador_rect: rect del jugador (para ajustar donde parese la bala)
        :param pantalla: valores de la pantalla del juego.

        """
        super().__init__()
        self.image = pygame.Surface((15, 30))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.pantalla = pantalla
        self.rect.centerx = jugador_rect.centerx
        self.rect.centery = jugador_rect.top
        self.velocidad = -5

    def update(self):
        """
        Metodo para actualizar el objeto Disparo.
        """
        self.rect.y += self.velocidad
        if self.rect.bottom < 0:
            self.kill()
        
    def dibujar(self):
        """
        Metodo que dibujar a el disparo.
        """
        self.pantalla.blit(self.image, self.rect)