import pygame

class Menu_creditos():
    """
    
    """
    def __init__(self):
        """
        """
        self.logo = pygame.image.load("assets/img/logo.png")
        self.boton_volver_menu = pygame.Rect(275, 500, 250, 50)

    
    def mostrar_menu_desafios(self, pantalla: pygame.Surface):


        menu_creditos = True
        while menu_creditos:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver_menu.collidepoint(event.pos):
                        return #menu_desafios = False  
                    
            pantalla.fill((0, 0, 0))  

            font1 = pygame.font.Font(None, 36)
            font2 = pygame.font.Font(None, 28)
            pantalla.blit(self.logo, (200, 20))

            titulo2 = font1.render("Musica y Efectos de sonido", True, (255, 255, 255))
            pantalla.blit(titulo2, (200, 320))

            textomusica1 = font2.render("Musica sacada de la bibloteca", True, (255, 255, 255))
            pantalla.blit(textomusica1, (80, 360))
            textomusica1 = font2.render("gratuita de loudly.com", True, (255, 255, 255))
            pantalla.blit(textomusica1, (80, 380))

            textomusica2 = font2.render("efectos de sonido de", True, (255, 255, 255))
            pantalla.blit(textomusica2, (500, 360))
            textomusica2 = font2.render("freesound.org por: ", True, (255, 255, 255))
            pantalla.blit(textomusica2, (500, 380))

            textoloudly = font2.render("The Darkside y The Sun", True, (255, 255, 255))
            pantalla.blit(textoloudly, (80, 420))

            textofreesound = font2.render("ERH, MATRIXXX, ", True, (255, 255, 255))
            pantalla.blit(textofreesound, (500, 420))
            textofreesound = font2.render("BareForm, juskiddink", True, (255, 255, 255))
            pantalla.blit(textofreesound, (500, 450))



            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_volver_menu)
            texto_volver_menu = font1.render("Volver al Menú", True, (0, 0, 0))
            pantalla.blit(texto_volver_menu, (310, 510))
            pygame.display.flip()

