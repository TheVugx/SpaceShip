import pygame
import sys
from menu import Menu
from musica import Musica

class Menu_muerte():
    """
    clase Menu Muerte, este es el Menu que aparece al morir en el juego.
    """
    def __init__(self,musica: Musica, juego):
        """
        Contructor de la Clase Menu Muerte.\n
        :param musica: Una instancia de la clase musica.
        """
        self.juego = juego
        self.menu = Menu(musica)
        self.logo = pygame.image.load("assets/img/logo.png")
        self.boton_puntaje = pygame.Rect(300, 200, 200, 50)
        self.boton_volver_a_jugar = pygame.Rect(300, 300, 200, 50)
        self.boton_salir_menu = pygame.Rect(300, 400, 200, 50)
        
    def mostrar_menu_muerte(self, pantalla: pygame.Surface, puntaje_valor: int):  #tipo_enemigo
        """
        Metodo que se encarga en mostrar el menu de muerte.\n
        :param pantalla: valores de la pantalla del juego.
        :param puntaje_valor: el valor de puntaje que el jugador logro al morir.
        """
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver_a_jugar.collidepoint(event.pos):
                        menu = False
                        return
                    elif self.boton_salir_menu.collidepoint(event.pos):
                        menu = False
                        puntaje_valor = 1
                        self.menu.mostrar_menu(pantalla, self.juego)
            font = pygame.font.Font(None, 38)
            fontEspecial = pygame.font.Font(None, 76)
            pantalla.blit(self.logo, (200, 20))

            texto_gameover = fontEspecial.render("Gameover", True, (255, 255, 255))
            pantalla.blit(texto_gameover, (265, 120))

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_puntaje)
            texto_puntaje = font.render("Puntaje: "+str(puntaje_valor), True, (0, 0, 0))
            pantalla.blit(texto_puntaje, (310, 210))

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_volver_a_jugar)
            texto_volver_a_jugar = font.render(" Volver a Jugar ", True, (0, 0, 0))
            pantalla.blit(texto_volver_a_jugar, (305, 310))

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_salir_menu)
            texto_salir_menu = font.render("Salir", True, (0, 0, 0))
            pantalla.blit(texto_salir_menu, (370, 410))

            pygame.display.flip()