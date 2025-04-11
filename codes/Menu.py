import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.Const import MENU_OPTION


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.surf = pygame.image.load('./asset/2op3.png')
        self.rect = self.surf.get_rect(left=0,top=0)
    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.tela.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, "Tic Tac Toe", (160, 32, 240), (288, 150))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30,MENU_OPTION[i], (177, 156, 217), (288, 230+30*i))
                else:
                    self.menu_text(30, MENU_OPTION[i], (255, 255, 255), (288, 230 + 30 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        if menu_option<len(MENU_OPTION)-1:
                            menu_option+=1
                        else:
                            menu_option = 0

            pygame.display.flip()

    def menu_text(self,text_size:int,text:str,text_color:tuple,text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name='Arial Bold',size=text_size)
        text_surf:Surface=text_font.render(text,True,text_color).convert_alpha()
        text_rect:Rect=text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf,dest=text_rect)