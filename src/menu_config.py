import pygame

from musica import Musica

class Menu_config():
    """
    clase Menu configuraciones, este es el Menu donde agustar el volumen.
    """
    def __init__(self,musica: Musica):
        """
        Contructor de la Clase Menu Configuraciones.\n
        :param musica: Una instancia de la clase musica.
        """
        self.musica = musica
        self.valor_volumen_juego = 0.5
        self.valor_volumen_menu = 0.5
        self.valor_volumen_efectos = 0.4
        self.barra_menu = pygame.Rect(370, 200, 300, 10)
        self.barra_juego = pygame.Rect(370, 250, 300, 10)
        self.barra_efectos = pygame.Rect(370, 300, 300, 10)
        self.boton_aplicar = pygame.Rect(130, 500, 200, 50) 
        self.boton_volver = pygame.Rect(470, 500, 200, 50)

    def actualizar_volumen_musica_game(self, nuevo_volumen: float):
        """
        metodo para actualizar el volumen de la musica principal del juego.\n
        :param nuevo_volumen: valor float para establece el volumen.
        """
        self.musica.establecer_volumen_musica_game(nuevo_volumen)
    
    def actualizar_volumen_musica_menu(self, nuevo_volumen: float):
        """
        metodo para actualizar el volumen de la musica del menu del juego.\n
        :param nuevo_volumen: valor float para establece el volumen.
        """
        self.musica.establecer_volumen_musica_menu(nuevo_volumen)
    
    def actualizar_volumen_efectos(self, nuevo_volumen: float):
        """
        metodo para actualizar el volumen de los efectos de sonido del juego.\n
        :param nuevo_volumen: valor float para establece el volumen.
        """
        self.musica.establecer_volumen_efectos_son(nuevo_volumen)
        
    def mostrar_menu_config(self, pantalla: pygame.Surface):
        """
        Metodo para mostrar el menu de configuraciones.\n
        :param pantalla: valores de la pantalla del juego.
        """
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.barra_menu.collidepoint(event.pos):
                        # El jugador hizo clic en la barra, actualiza el valor del control deslizante
                        x_mouse, _ = event.pos
                        self.valor_volumen_menu = (x_mouse - self.barra_menu.left) / self.barra_menu.width
                        self.valor_volumen_menu = max(0, min(1, self.valor_volumen_menu))
                    if self.barra_juego.collidepoint(event.pos):
                        # El jugador hizo clic en la barra, actualiza el valor del control deslizante
                        x_mouse, _ = event.pos
                        self.valor_volumen_juego = (x_mouse - self.barra_juego.left) / self.barra_juego.width
                        self.valor_volumen_juego = max(0, min(1, self.valor_volumen_juego)) 
                    if self.barra_efectos.collidepoint(event.pos):
                        # El jugador hizo clic en la barra, actualiza el valor del control deslizante
                        x_mouse, _ = event.pos
                        self.valor_volumen_efectos = (x_mouse - self.barra_efectos.left) / self.barra_efectos.width
                        self.valor_volumen_efectos = max(0, min(1, self.valor_volumen_efectos)) 
                    if self.boton_volver.collidepoint(event.pos):
                        return
                    if self.boton_aplicar.collidepoint(event.pos):
                        self.actualizar_volumen_musica_game(self.valor_volumen_juego)
                        self.actualizar_volumen_musica_menu(self.valor_volumen_menu)
                        self.actualizar_volumen_efectos(self.valor_volumen_efectos)


            pantalla.fill((0, 0, 0))
            font = pygame.font.Font(None, 38)

            logo = pygame.image.load("assets/img/logo.png")
            pantalla.blit(logo, (200, 20))

          

            texto_menu = font.render("Musica Menu", True, (255, 255, 255))
            pantalla.blit(texto_menu, (120, 200))

            pygame.draw.rect(pantalla, (255, 255, 255), self.barra_menu)
            marcador_x1 = self.barra_menu.left + int(self.barra_menu.width * self.valor_volumen_menu)
            pygame.draw.circle(pantalla, (255, 255, 255), (marcador_x1, self.barra_menu.centery), 10)


            texto2 = font.render("Musica Juego", True, (255, 255, 255))
            pantalla.blit(texto2, (120, 250))

            pygame.draw.rect(pantalla, (255, 255, 255), self.barra_juego)
            marcador_x2 = self.barra_juego.left + int(self.barra_juego.width * self.valor_volumen_juego)
            pygame.draw.circle(pantalla, (255, 255, 255), (marcador_x2, self.barra_juego.centery), 10)


            texto3 = font.render("Efectos", True, (255, 255, 255))
            pantalla.blit(texto3, (120, 300))

            pygame.draw.rect(pantalla, (255, 255, 255), self.barra_efectos)
            marcador_x3 = self.barra_efectos.left + int(self.barra_efectos.width * self.valor_volumen_efectos)
            pygame.draw.circle(pantalla, (255, 255, 255), (marcador_x3, self.barra_efectos.centery), 10)

            texto_controlles = font.render("Controlles", True, (255, 255, 255))
            pantalla.blit(texto_controlles, (120, 350))

            controlles1 = font.render("    A - D     Movimiento", True, (0, 0, 0), (255,255,255))
            pantalla.blit(controlles1, (370, 350))

            controlles2 = font.render("   Espacio     Dispar     ", True, (0, 0, 0), (255,255,255))
            pantalla.blit(controlles2, (370, 380))            

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_aplicar)
            texto_aplicar = font.render(" Aplicar ", True, (0, 0, 0))
            pantalla.blit(texto_aplicar, (150, 510))

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_volver)
            texto_volver = font.render(" Volver ", True, (0, 0, 0))
            pantalla.blit(texto_volver, (520, 510))


            pygame.display.flip()

        pygame.quit()