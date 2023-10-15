import pygame

class Disparo(pygame.sprite.Sprite):
    """
    clase Disparo.
    """
    def __init__(self, jugador_rect: pygame.Rect):
        """
        constructor de la clase Disparo.\n
        :param jugador_rect: rect del jugador (para ajustar donde parese la bala)
        """
        super().__init__()
        self.image = pygame.Surface((15, 30))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
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
        
    def dibujar(self,pantalla):
        """
        Metodo que dibujar a el disparo.
        """
        pantalla.blit(self.image, self.rect)