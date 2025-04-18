import pygame
from pygame import Surface, Rect
from pygame.font import Font
from codes.Const import MENU_OPTION
from codes.DB import DB


class Menu:
#Carrega a telinha do jogo no menu com a imagem de background
    def __init__(self, tela):
        self.tela = tela
        self.surf = pygame.image.load('./asset/2op2.png')
        self.rect = self.surf.get_rect(left=0,top=0)
        self.db = DB('DB_nome.db')

#Adiciona a musica em loop junto com as informacoes da tela do menu
    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.tela.fill((0, 0, 0))
            self.tela.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, "Tic Tac Toe", (177, 156, 217), (288, 50))
            mutar_rect = self.menu_text(20, "<-Mutar", (255, 255, 255), (40, 70))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30,MENU_OPTION[i], (160, 32, 240), (288, 230+30*i))
                else:
                    self.menu_text(30, MENU_OPTION[i], (255, 255, 255), (288, 230 + 30 * i))
            pygame.display.flip()

#Eventos que tornam o jogo funcional (selecionar a funcao desejada)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.db.reset()  # Limpa os dados
                    self.db.close()
                    pygame.quit()
                    quit() #fechar

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option<len(MENU_OPTION)-1:
                            menu_option += 1
                        else:
                            menu_option = 0 #Seta para baixo
                    if event.key == pygame.K_UP:
                        if menu_option>0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION)-1 #Seta para cima
                    if event.key == pygame.K_RETURN:
                        return  MENU_OPTION[menu_option]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  #verifica se o clique e no botao esquerdo
                        mouse_pos = pygame.mouse.get_pos()
                        if mutar_rect.collidepoint(mouse_pos):
                            pygame.mixer_music.stop()

    def menu_text(self,text_size:int,text:str,text_color:tuple,text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name='arial',size=text_size)
        text_surf:Surface=text_font.render(text,True,text_color).convert_alpha()
        text_rect:Rect=text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf,dest=text_rect)
        return text_rect