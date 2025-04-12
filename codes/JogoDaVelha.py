import pygame
from pygame import Surface, Rect
from pygame.font import Font

#Desenha o tabuleiro
def grade_tabuleiro(tela):
    pygame.draw.line(tela, (255,255,255),(105,100),(105,300),6)
    pygame.draw.line(tela, (255,255,255),(205,100),(205,300),6)
    pygame.draw.line(tela, (255,255,255),(100,105),(300,105),6)
    pygame.draw.line(tela, (255,255,255),(100,205),(300,205),6)


class JogoDaVelha:
    def __init__(self, tela, tela_nome, menu_option):
        self.tela = tela
        self.tela_nome = tela_nome
        self.menu_option = menu_option

        self.surf = pygame.image.load('./asset/3op3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)
        voltar_rect = None

        while True:
            self.tela.fill((0, 0, 0))  # Limpa a tela com preto
            self.tela.blit(source=self.surf, dest=self.rect)

            voltar_rect = self.menu_text(20, "<-Menu", (255,255,255), (40, 30))

            self.menu_text(50, "Jogo da Velha", (160, 32, 240), (288, 90))

            grade_tabuleiro(self.tela)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() #fechar
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #verifica se o clique e no botao esquerdo
                        mouse_pos = pygame.mouse.get_pos() #pega a posicao do botao
                        if voltar_rect.collidepoint(mouse_pos): #verifica se o clique foi no botao
                            return #faz o botao retornar ao Menu

    def menu_text(self,text_size:int,text:str,text_color:tuple,text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name='arial',size=text_size)
        text_surf:Surface=text_font.render(text,True,text_color).convert_alpha()
        text_rect:Rect=text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf,dest=text_rect)
        return text_rect

