import pygame
from pygame import Surface, Rect
from pygame.font import Font


class JogoDaVelha:
    def __init__(self, tela, name, menu_option):
        self.tela = tela
        self.name = name
        self.menu_option = menu_option

        self.surf = pygame.image.load('./asset/3op3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.tela.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, "Jogo da Velha", (160, 32, 240), (288, 150))

    def menu_text(self,text_size:int,text:str,text_color:tuple,text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name='Arial Bold',size=text_size)
        text_surf:Surface=text_font.render(text,True,text_color).convert_alpha()
        text_rect:Rect=text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf,dest=text_rect)