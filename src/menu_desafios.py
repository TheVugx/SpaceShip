import pygame


class Menu_desafios():
    """
    clase Menu desafios, este es el Menu nivele, donde se muestran los distintos desafios.
    """
    def __init__(self):
        """
        Contructor de la Clase Menu desafios.\n
        """
        self.logo = pygame.image.load("assets/img/logo.png")
        self.img_des_0 = pygame.image.load("assets/img/ch__.png")
        self.img_des_1 = pygame.image.load("assets/img/ch_1.png")
        self.img_des_2 = pygame.image.load("assets/img/ch_2.png")
        self.img_des_3 = pygame.image.load("assets/img/ch_3.png")
        self.img_des_4 = pygame.image.load("assets/img/ch_4.png")
        self.img_des_5 = pygame.image.load("assets/img/ch_5.png")
        self.img_des_6 = pygame.image.load("assets/img/ch_6.png")
        self.img_des_7 = pygame.image.load("assets/img/ch_7.png")


        self.boton_des_1 = pygame.Rect(100, 170, 50, 50)
        self.boton_des_2 = pygame.Rect(200, 170, 50, 50)
        self.boton_des_3 = pygame.Rect(300, 170, 50, 50)
        self.boton_des_4 = pygame.Rect(400, 170, 50, 50)
        self.boton_des_5 = pygame.Rect(500, 170, 50, 50)
        self.boton_des_6 = pygame.Rect(600, 170, 50, 50)
        self.boton_des_7 = pygame.Rect(100, 270, 50, 50)
        self.boton_des_8 = pygame.Rect(200, 270, 50, 50)
        self.boton_des_9 = pygame.Rect(300, 270, 50, 50)
        self.boton_des_10 = pygame.Rect(400, 270, 50, 50)
        self.boton_des_11 = pygame.Rect(500, 270, 50, 50)
        self.boton_des_12 = pygame.Rect(600, 270, 50, 50)
        self.boton_des_13 = pygame.Rect(100, 370, 50, 50)
        self.boton_des_14 = pygame.Rect(200, 370, 50, 50)
        self.boton_des_15 = pygame.Rect(300, 370, 50, 50)
        self.boton_des_16 = pygame.Rect(400, 370, 50, 50)
        self.boton_des_17 = pygame.Rect(500, 370, 50, 50)
        self.boton_des_18 = pygame.Rect(600, 370, 50, 50)

        self.boton_volver_menu = pygame.Rect(275, 500, 250, 50)

    def mostrar_menu_desafios(self, pantalla: pygame.Surface, juego):
        """
        Metodo que se encarga en mostrar el menu de desafios.\n
        :param pantalla: valores de la pantalla del juego.
        """
        menu_desafios = True
        while menu_desafios:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver_menu.collidepoint(event.pos):
                        return #menu_desafios = False  
                    if self.boton_des_1.collidepoint(event.pos):
                        juego.iniciar(100)
                        juego.gameloop(20,1,100)
                    if self.boton_des_2.collidepoint(event.pos):
                        juego.iniciar(3,["cuadrado"])
                        juego.gameloop(200,1050,7,1,1,["cuadrado"])
                    if self.boton_des_3.collidepoint(event.pos):
                        juego.iniciar(3,["rectangular"])
                        juego.gameloop(200,1050,7,1,1,["rectangular"])
                    if self.boton_des_4.collidepoint(event.pos):
                        juego.iniciar(3,["circular"])
                        juego.gameloop(200,1050,7,1,1,["circular"])    
                    if self.boton_des_5.collidepoint(event.pos):
                        juego.iniciar(3,["hexagonal"])
                        juego.gameloop(200,1050,7,1,1,["hexagonal"])
                    if self.boton_des_6.collidepoint(event.pos):
                        juego.iniciar(3,["octagonal"])
                        juego.gameloop(200,1050,7,1,1,["octagonal"])


            pantalla.fill((0, 0, 0))  

            font = pygame.font.Font(None, 36)
            pantalla.blit(self.logo, (200, 20))
            

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_1)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_2)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_3)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_4)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_5)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_6)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_7)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_8)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_9)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_10)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_11)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_12)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_13)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_14)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_15)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_16)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_17)
            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_des_18)

            pantalla.blit(self.img_des_1, (100, 170))
            pantalla.blit(self.img_des_2, (200, 170))
            pantalla.blit(self.img_des_3, (300, 170))
            pantalla.blit(self.img_des_4, (400, 170))
            pantalla.blit(self.img_des_5, (500, 170))
            pantalla.blit(self.img_des_6, (600, 170))
            pantalla.blit(self.img_des_7, (100, 270))
            pantalla.blit(self.img_des_0, (200, 270))
            pantalla.blit(self.img_des_0, (300, 270))
            pantalla.blit(self.img_des_0, (400, 270))
            pantalla.blit(self.img_des_0, (500, 270))
            pantalla.blit(self.img_des_0, (600, 270))
            pantalla.blit(self.img_des_0, (100, 370))
            pantalla.blit(self.img_des_0, (200, 370))
            pantalla.blit(self.img_des_0, (300, 370))
            pantalla.blit(self.img_des_0, (400, 370))
            pantalla.blit(self.img_des_0, (500, 370))
            pantalla.blit(self.img_des_0, (600, 370))

            pygame.draw.rect(pantalla, (255, 255, 255), self.boton_volver_menu)
            texto_volver_menu = font.render("Volver al Menú", True, (0, 0, 0))
            pantalla.blit(texto_volver_menu, (310, 510))

            pygame.display.flip()