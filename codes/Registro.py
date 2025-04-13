
import pygame
from pygame import Surface, Rect, K_RETURN, K_TAB, K_BACKSPACE
from pygame.font import Font

from codes.DB import DB


class Registro:
    def __init__(self, tela,tela_nome,menu_option):
        self.tela = tela
        self.tela_nome = tela_nome
        self.menu_option = menu_option

        self.surf = pygame.image.load('./asset/2op4.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        self.nome = ""
        self.genero = ""
        self.campo_ativo = "nome"

    def run(self):

        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)
        voltar_rect = None
        db = DB('DB_nome.db')

        while True:
            self.tela.fill((0, 0, 0))  # Limpa a tela com preto
            self.tela.blit(source=self.surf, dest=self.rect)

            voltar_rect = self.menu_text(20, "<-Menu", (255, 255, 255), (40, 30))
            mutar_rect = self.menu_text(20, "<-Mutar", (255, 255, 255), (40, 70))

            self.menu_text(50, "Registro", (160, 32, 240), (288, 90))
            self.menu_text(30, "Apelido", (255, 255, 255), (288, 150))
            self.menu_text(30, "Genero", (255, 255, 255), (288, 220))
            self.menu_text(25, self.nome + ("|" if self.campo_ativo == "nome" else ""), (255, 255, 0), (288, 180))
            self.menu_text(25, self.genero + ("|" if self.campo_ativo == "genero" else ""), (255, 255, 0), (288, 250))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() #fechar

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  #verifica se o clique e no botao esquerdo
                        mouse_pos = pygame.mouse.get_pos()  #pega a posicao do botao
                        if voltar_rect.collidepoint(mouse_pos):  #verifica se o clique foi no botao
                            return  #faz o botao retornar ao Menu
                        if mutar_rect.collidepoint(mouse_pos):
                            pygame.mixer_music.stop()

                if event.type == pygame.KEYDOWN:
                        if event.key == K_TAB:
                            # Alterna entre os campos para escrever genero e nome
                            self.campo_ativo = "genero" if self.campo_ativo == "nome" else "nome"

                        elif event.key == K_RETURN:
                            if self.nome.strip() and self.genero.strip():
                                db.save(self.nome, self.genero)
                                self.nome = ""
                                self.genero = "" #ao apertar enter salva no BD
                            else:
                                print("Preencha todos os campos.")

                        elif event.key == K_BACKSPACE:
                            if self.campo_ativo == "nome":
                                self.nome = self.nome[:-1]
                            else:
                                self.genero = self.genero[:-1] #apaga o ultimo caracter se der backspace

                        else:
                            char = event.unicode
                            if char.isprintable():
                                if self.campo_ativo == "nome":
                                    self.nome += char
                                else:
                                    self.genero += char  #permite a escrita


    def menu_text(self,text_size:int,text:str,text_color:tuple,text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name='arial',size=text_size)
        text_surf:Surface=text_font.render(text,True,text_color).convert_alpha()
        text_rect:Rect=text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf,dest=text_rect)
        return text_rect