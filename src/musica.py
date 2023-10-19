import pygame.mixer
import pygame.mixer_music
import random


class Musica():
    """
    Clase Musica, que carga y reproduce musica, efectos de sonidos, control de volumen.
    """
    def __init__(self):
        """
        Constructor de clase musica
        """
        pygame.mixer.init()
        self.volumen_musica_menu = 0.5
        self.volumen_musica_game = 0.5
        self.volumen_efectos_son = 0.5
        
        self.son_efect = "assets/sonidos/efectos_de_sonido/"

        self.bum = [pygame.mixer.Sound(self.son_efect + "/bareform__boom-bang.aiff"),
                    pygame.mixer.Sound(self.son_efect + "/juskiddink__distant-explosion.wav")]
        
        self.disparos =[pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-01.wav"),
                        pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-02.wav"),
                        pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-03.wav"),
                        pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-04.wav"),
                        pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-05.wav"),
                        pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-06.wav"),
                        pygame.mixer.Sound(self.son_efect + "/matrixxx__retro-laser-shot-07.wav")]
        
        self.efectos = [pygame.mixer.Sound(self.son_efect +  "/erh__boom-1.wav"),
                        pygame.mixer.Sound(self.son_efect +  "/erh__boom-2.wav"),
                        pygame.mixer.Sound(self.son_efect +  "/erh__boom-3.wav"),
                        pygame.mixer.Sound(self.son_efect +  "/erh__pulsar.wav"),
                        pygame.mixer.Sound(self.son_efect +   "/erh__raw-2.wav"),
                        pygame.mixer.Sound(self.son_efect +     "/erh__raw.wav"),
                        pygame.mixer.Sound(self.son_efect + "/erh__tension.wav")]

    def iniciar_musica(self):
        """
        Metodo que inicia la musica principal del juego en bucle.
        """
        pygame.mixer.music.load("assets/sonidos/musica/The_Sun.mp3") 
        pygame.mixer.music.set_volume(self.volumen_musica_game) 
        pygame.mixer.music.play(-1)

    def detener_musica(self):
        """
        Metodo que detiene la musica principal del juego.
        """
        pygame.mixer.music.stop()

    def iniciar_musica_menu(self):
        """
        Metodo que inicia la musica del menu en bucle.
        """
        pygame.mixer.music.load("assets/sonidos/musica/The_Darkside.mp3")
        pygame.mixer.music.set_volume(self.volumen_musica_menu)
        pygame.mixer.music.play(-1)

    def detener_musica_menu(self):
        """
        Metodo que detiene la musica del menu.
        """
        pygame.mixer.music.stop()

    def play_boom(self):
        """
        Metodo que elige un sonido de explocion al azar y lo reproduce 
        """
        self.boom = random.choice(self.bum)
        self.boom.set_volume(self.volumen_efectos_son)
        self.boom.play()

    def play_disparo(self):
        """
        Metodo que elige un sonido de disparo al azar y lo reproduce 
        """
        self.disparo = random.choice(self.disparos)
        self.disparo.set_volume(self.volumen_efectos_son)
        self.disparo.play()

    def play_efecto(self):
        """
        Metodo que elige un efecto de sonido al azar y lo reproduce 
        """
        self.efecto = random.choice(self.efectos)
        self.efecto.set_volume(self.volumen_efectos_son)
        self.efecto.play()
    
    def play_bonificacion(self):
        """
        Metodo que elige un sonido de bonificacion al azar y lo reproduce 
        """
        self.bonificacion = pygame.mixer.Sound(self.son_efect + "matrixxx__cheerful.wav")
        self.bonificacion.set_volume(self.volumen_efectos_son)
        self.bonificacion.play()

    def establecer_volumen_musica_game(self, nuevo_volumen: float):
        """
        Metodo que establece el volumen de la musica principal del juego\n
        :param nuevo_volumen: valor float para establece el volumen.
        """
        self.volumen_musica_game = nuevo_volumen

    def establecer_volumen_musica_menu(self, nuevo_volumen: float):
        """
        Metodo que establece el volumen de la musica del menu\n
        :param nuevo_volumen: valor float para establece el volumen.
        """
        self.volumen_musica_menu = nuevo_volumen

    def establecer_volumen_efectos_son(self, nuevo_volumen: float):
        """
        Metodo que establece el volumen de los efectos de sonido del juego\n
        :param nuevo_volumen: valor float para establece el volumen.
        """
        self.volumen_efectos_son = nuevo_volumen
