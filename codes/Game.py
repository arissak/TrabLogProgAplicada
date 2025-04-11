from codes.Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size=(576, 324))

    def run(self):
    # Necessario para chamar o menu
        while True:
            menu = Menu(self.tela)
            menu.run()
