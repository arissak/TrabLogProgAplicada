from codes.Const import MENU_OPTION
from codes.Menu import Menu
import pygame
from codes.JogoDaVelha import JogoDaVelha

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size=(576, 324))

    def run(self):
    # Necessario para chamar o menu
        while True:
            menu = Menu(self.tela)
            menu_return = menu.run()

            #Checar qual funcionalidade rodar
            if menu_return == MENU_OPTION[0]:
                jogo = JogoDaVelha(self.tela,'Jogo da Velha', menu_return)
                jogo_return = jogo.run()
            else:
                pass
