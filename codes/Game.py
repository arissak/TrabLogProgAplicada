from codes.Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size=(600, 480))

    def run(self):
    # Necessario para deixar a tela aberta e porder fechar quando quiser
        while True:
            menu = Menu(self.tela)
            menu.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()