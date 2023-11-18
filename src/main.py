import pygame
import random

from jugador import Jugador
from menu import Menu
from menu_muerte import Menu_muerte
from ges_enemigos import ges_enemigos
from ges_bonificaciones import ges_bonificaciones
from musica import Musica

class Main():
    """
    Clase main.
    """
    def __init__(self):
        """
        Constructor de clase main.
        """
        pygame.init()
        self.musica = Musica()
        self.ANCHO, self.ALTO = 800, 600
        self.FPS = 60
        self.puntaje_anterior = 1
        self.gametick = 1

        self.menu_muerte = Menu_muerte(self.musica, self)
        self.menu = Menu(self.musica)

        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("SpaceShip")

        self.icono = pygame.image.load("assets/img/icono.png")
        pygame.display.set_icon(self.icono)

        self.jugador = Jugador(self.pantalla)

        self.grupo_enemigos = pygame.sprite.Group()
        self.grupo_bonificaciones = pygame.sprite.Group()
        self.grupo_balas = pygame.sprite.Group()

        self.reloj = pygame.time.Clock()

        self.in_bon = ges_bonificaciones()

        self.jugando = True
        self.movimiento_izquierda = False
        self.movimiento_derecha = False



    def iniciar(self, disparos = 2, lista_enemigos = ["rectangular","cuadrado", "octagonal", "hexagonal"]):
        """
        Metodo que inicializa variables para iniciar el juego
        :param disparos: cantidad de disparos que quires que inicialice el jugador
        :param lista_enemigos: lista de enemigos que el gameloop va a manejar
        """
        self.musica.detener_musica_menu()
        self.musica.iniciar_musica()
        self.jugador.iniciar_puntaje()
        self.jugador.iniciar_disparo(disparos)
        self.jugador.repocicionar()
        self.grupo_enemigos.empty()
        self.grupo_bonificaciones.empty()
        self.grupo_balas.empty()
        self.jugando = True
        self.movimiento_izquierda = False
        self.movimiento_derecha = False
        self.puntaje_anterior = 1
        self.gametick = 1
        self.in_ene = ges_enemigos(lista_enemigos)


    def iniciar_objetos(self, cantidad_en: int, cantidad_bon: int):
        """
        Metodo que crea enemigos y/o bonificaciones.\n
        :param cantidad_en: numero para definir cuantos enemigos crear
        :param cantidad_bon: numero para definir cuantas bonificaciones crear
        """
        for i in range(cantidad_en):
            self.grupo_enemigos.add(self.in_ene.iniciar_enemigos(self.pantalla))
        for i in range(cantidad_bon):
            self.grupo_bonificaciones.add(self.in_bon.iniciar_bonificaciones(self.pantalla))
        

    def control_objetos(self, disparos: int, lista_enemigos):
        """
        Metodo que actualizar y dibujar todos los objetos en la pantalla, balas, jugador, enemigos y bonificaciones.\n
        :param disparos: numero de cantidad de balas que da una bonifiacion de disparos
        :param lista_enemigos: lista de enemigos que el gameloop va a manejar
        """
        self.grupo_balas.update()
        self.jugador.update()
        self.grupo_enemigos.update()
        self.grupo_bonificaciones.update()

        self.pantalla.fill((0, 0, 0))

        self.jugador.dibujar() 
        for bala in self.grupo_balas:
            bala.dibujar()
        for enemigo in self.grupo_enemigos:
            enemigo.dibujar()
        for bonificaciones in self.grupo_bonificaciones:
            bonificaciones.dibujar()

        for bala in self.grupo_balas:
            for enemigo in self.grupo_enemigos:
                self.colisiones_balas = pygame.sprite.collide_mask(enemigo, bala)
                if self.colisiones_balas:
                    self.musica.play_boom()
                    if not enemigo.colisionada:
                        height = enemigo.rect.height
                        width = enemigo.rect.width
                        enemigo.kill()
                        bala.kill()
                        self.jugador.aumentar_puntaje(int((height+width)/3))
                        enemigo.colisionada = True

        for bonificacion in self.grupo_bonificaciones:
            self.colisiones_bonificaciones = pygame.sprite.collide_mask(self.jugador, bonificacion)
            if self.colisiones_bonificaciones and not bonificacion.recolectada:
                self.musica.play_bonificacion()
                self.recolectada = True
                if bonificacion.puntos == 0:
                    self.jugador.aumentar_disparo(disparos)
                    bonificacion.kill()
                else:
                    self.jugador.aumentar_puntaje(bonificacion.puntos)
                    bonificacion.kill()


        for enemigo in self.grupo_enemigos:
            self.colisiones = pygame.sprite.collide_mask(self.jugador, enemigo)
            if self.colisiones:
                self.jugando = False
                self.musica.detener_musica()
                self.menu_muerte.mostrar_menu_muerte(self.pantalla, self.jugador.puntaje)
                self.iniciar(disparos, lista_enemigos)
            
    def control_puntaje(self):
        """
        Metodo que controla y dibuja el puntaje de un jugador.
        """
        #aumenta el puntaje del jugador
        self.gametick += 1
        if (self.gametick % 20) == 0:
            self.jugador.aumentar_puntaje(1)

        font = pygame.font.Font(None, 36)
        texto_puntaje = font.render("Puntaje: "+str(self.jugador.puntaje) + (str(" █") * self.jugador.disparo), True, (255, 255, 255))
        self.pantalla.blit(texto_puntaje, (0, 0)) 

    def generar_objetos(self,tick_enemigos: int, tick_bonificaciones: int):
        """
        Metodo que genera nuevos objetos al avanzar cada gameloop.\n
        :param tick_enemigos: cada cuantos tick se genera un enemigo.
        :param tick_bonificaciones: cada cuantos tick se genera una bonificacion.
        """
        ##     generar mas objetos en pantalla cada cierto gameticks     # 
        if self.gametick % tick_enemigos == 0 and self.gametick != self.puntaje_anterior:
            self.puntaje_anterior = self.jugador.puntaje
            self.iniciar_objetos(1,0)
        if self.gametick % tick_bonificaciones == 0 and self.gametick != self.puntaje_anterior:
            self.puntaje_anterior = self.jugador.puntaje
            self.iniciar_objetos(0,1)
        if self.gametick % 200 == 0 and self.gametick != self.puntaje_anterior:
            if random.randrange(1,8,1) == 6:
                self.musica.play_efecto()

        

    def gameloop(self, tick_ene: int, tick_bon:int, ini_en: int, ini_bon = 1, disparos = 1,
                 lista_enemigos = ["rectangular","cuadrado", "octagonal", "hexagonal"]):
        """
        Metodo que carga el gameloop principal.\n
        :param tick_ene: cada cuantos tick se genera un enemigo.
        :param tick_bon: cada cuantos tick se genera una bonificacion.
        :param ini_en: cantidad de enemigos que se generan en los primeros tick.
        :param ini_bon: cantidad de bonificaciones que se generan en los primeros tick (recomendado dejar en 1).
        :param disparos: cantidad de balas que aumenta al recojer una bonificacion de municion
        :param lista_enemigos: lista de enemigos que el gameloop va a manejar
        """
        while self.jugando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jugando = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movimiento_izquierda = True
                    elif event.key == pygame.K_d:
                        self.movimiento_derecha = True
                    elif event.key == pygame.K_SPACE:
                        if self.jugador.disparo >= 1:
                            self.grupo_balas.add(self.jugador.disparar(self.musica))
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movimiento_izquierda = False
                    elif event.key == pygame.K_d:
                        self.movimiento_derecha = False
                
            if self.movimiento_izquierda:
                self.jugador.mover_izquierda()
            if self.movimiento_derecha:
                self.jugador.mover_derecha()

            if self.gametick == 2:
                self.iniciar_objetos(ini_en, ini_bon)
                
            self.control_objetos(disparos, lista_enemigos)
            self.control_puntaje()
            self.generar_objetos(tick_ene,tick_bon)
            pygame.display.flip()
            self.reloj.tick(self.FPS)
        pygame.quit()


juego = Main()

juego.menu.mostrar_menu(juego.pantalla, juego)
juego.iniciar()
juego.gameloop(200,1050,7,1,1)


