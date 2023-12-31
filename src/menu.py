import pygame
import sys
from musica import Musica
from menu_desafios import Menu_desafios
from menu_config import Menu_config
from menu_creditos import Menu_creditos

class Menu():
    """
    clase Menu, este es el Menu principal del juego.
    """
    def __init__(self, musica: Musica):
        """
        Contructor de la Clase Menu.\n
        :param musica: Una instancia de la clase musica.
        """
        musica.iniciar_musica_menu()
        self.fondo_menu = pygame.image.load("assets/img/menu_principal.png")
        self.boton_comenzar = pygame.Rect(260, 140, 280, 50)
        self.boton_desafios = pygame.Rect(260, 210, 280, 50)
        self.boton_creditos = pygame.Rect(260, 280, 280, 50)
        self.boton_config = pygame.Rect(260, 350, 280, 50)
        self.boton_cerrar = pygame.Rect(260, 420, 280, 50)
        self.config = Menu_config(musica)
        self.config.valor_volumen_efectos
        self.config.valor_volumen_juego
        self.config.valor_volumen_menu
        self.menu_desafios = Menu_desafios()
        self.menu_creditos = Menu_creditos()


    def mostrar_menu(self, pantalla: pygame.Surface, juego, musica: Musica):
        """
        Metodo que se encarga en mostrar el menu principal
        :param pantalla: valores de la pantalla del juego.
        :param Musica: 
        """
        self.juego = juego
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_comenzar.collidepoint(event.pos):
                        menu = False
                    elif self.boton_desafios.collidepoint(event.pos):
                        self.desafios = self.menu_desafios.mostrar_menu_desafios(pantalla, self.juego)
                    elif self.boton_creditos.collidepoint(event.pos):
                        self.creditos = self.menu_creditos.mostrar_menu_desafios(pantalla)
                    elif self.boton_config.collidepoint(event.pos):
                        self.config.mostrar_menu_config(pantalla)
                    elif self.boton_cerrar.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()


            
            pantalla.fill((0, 0, 0))
            pantalla.blit(self.fondo_menu, (0, 0))
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_comenzar)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_desafios)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_creditos)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_config)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_cerrar)

            font = pygame.font.Font(None, 42)
            self.texto_comenzar = font.render("Jugar", True, (0, 0, 0))
            self.texto_desafios = font.render("Desafios", True, (0, 0, 0))
            self.texto_creditos = font.render("Creditos", True, (0, 0, 0))
            self.texto_config = font.render("Ajustes", True, (0, 0, 0))
            self.texto_cerrar = font.render("Salir", True, (0, 0, 0))
            pantalla.blit(self.texto_comenzar, (350, 150))
            pantalla.blit(self.texto_desafios, (350, 220))
            pantalla.blit(self.texto_creditos, (350, 290))
            pantalla.blit(self.texto_config, (350, 360))
            pantalla.blit(self.texto_cerrar, (370, 430))

            pygame.display.flip()
