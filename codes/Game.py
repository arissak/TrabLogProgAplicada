from codes.Const import MENU_OPTION
from codes.Menu import Menu
import pygame
from codes.JogoDaVelha import JogoDaVelha
from codes.Registro import Registro


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
            elif menu_return == MENU_OPTION[1]:
                registro = Registro(self.tela,'Registro',menu_return)
                registro_return = registro.run()
            else:
                pass
