import pygame
import sys


class Menu_registro():
    def __init__(self):
        pass

    def guardar_nombre(self, nombre):
        with open("nombre_usuario.txt", "w") as archivo:
            archivo.write(nombre)

    def cargar_nombre(self):
        try:
            with open("nombre_usuario.txt", "r") as archivo:
                nombre = archivo.read()
                return nombre
        except FileNotFoundError:
            return None

    def mostrar_menu_registro(self):
        pygame.init()
        
        pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Input de Texto")

        self.boton_jugar = pygame.Rect(300, 410, 200, 50)
        reloj = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        self.texto = ""

        self.menu = True
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Realizar alguna acción con el texto ingresado
                        print("Texto ingresado:", self.texto)
                        self.texto = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.texto = self.texto[:-1]
                        self.guardar_nombre(self.texto)
                        self.menu = False
                    else:
                        self.texto += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_jugar.collidepoint(event.pos):
                        self.guardar_nombre(self.texto)
                        self.menu = False
                    else:
                        pass
                    


            
            pantalla.fill((0, 0, 0))

            logo = pygame.image.load("assets/img/logo.png")
            pantalla.blit(logo, (200, 20))

            texto_base = font.render("Ingrese su NickName", True, (255,255,255))
            pantalla.blit(texto_base, (270, 200))
            
            texto_superficie = font.render(self.texto, True, (255,255,255))
            pantalla.blit(texto_superficie, (300, 340))
            if self.texto != '':
                pygame.draw.rect(pantalla, (255, 255, 255), self.boton_jugar)
                texto_jugar = font.render("Iniciar", True, (0, 0, 0))
                pantalla.blit(texto_jugar, (305, 410))

            pygame.display.flip()
            reloj.tick(30)
