import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.Const import centros_celulas


#Desenha o tabuleiro
def grade_tabuleiro(tela):
    pygame.draw.line(tela, (255,255,255),(238,12),(238,312),6)
    pygame.draw.line(tela, (255,255,255),(338,12),(338,312),6)
    pygame.draw.line(tela, (255,255,255),(138,112),(438,112),6)
    pygame.draw.line(tela, (255,255,255),(138,212),(438,212),6)


class JogoDaVelha:
    def __init__(self, tela, tela_nome, menu_option):
        self.tela = tela
        self.tela_nome = tela_nome
        self.menu_option = menu_option

        self.surf = pygame.image.load('./asset/3op3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        self.tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]

        self.rects_celulas = [
            [pygame.Rect(x - 32, y - 32, 65, 65) for (x, y) in linha]
            for linha in centros_celulas
        ]

    def run(self):
        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)

        player1 = True

        while True:
            self.tela.fill((0, 0, 0))  # Limpa a tela com preto
            self.tela.blit(source=self.surf, dest=self.rect)

            voltar_rect = self.menu_text(20, "<-Menu", (255,255,255), (40, 30))

            self.menu_text(20, "Jogo da Velha", (160, 32, 240), (500, 30))

            for i in range(3):  # 3 linhas
                for j in range(3):
                    centro = centros_celulas[i][j]

                    botao_img = pygame.image.load('./asset/fig12.png').convert_alpha()
                    img_redimensionada = pygame.transform.scale(botao_img, (65,65))
                    botao_rect = img_redimensionada.get_rect(center=centro)
                    self.tela.blit(img_redimensionada, botao_rect)

                    if self.tabuleiro[i][j]:
                        img_jogador = pygame.image.load(self.tabuleiro[i][j]).convert_alpha()
                        img_jogador = pygame.transform.scale(img_jogador, (65, 65))
                        self.tela.blit(img_jogador, botao_rect)

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

                        for i in range(3):
                            for j in range(3):
                                if self.rects_celulas[i][j].collidepoint(mouse_pos) and not self.tabuleiro[i][j]:
                                    # Se a célula estiver vazia, registra o movimento
                                    if player1:
                                        self.tabuleiro[i][j] = './asset/fig19.png'  #Img para player1
                                    else:
                                        self.tabuleiro[i][j] = './asset/fig15.png'  #Img para player2

                                    player1 = not player1  # Alterna entre os jogadores
                                    break  # Sai do loop de verificação de células

    def menu_text(self,text_size:int,text:str,text_color:tuple,text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name='arial',size=text_size)
        text_surf:Surface=text_font.render(text,True,text_color).convert_alpha()
        text_rect:Rect=text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf,dest=text_rect)
        return text_rect

