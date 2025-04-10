import pygame


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.surf = pygame.image.load('./asset/2op3.png')
        self.rect = self.surf.get_rect(left=0,top=0)
    def run(self):
        self.tela.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()