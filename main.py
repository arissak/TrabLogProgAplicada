import pygame

pygame.init()

tela = pygame.display.set_mode(size=(600,480))

# Necessario para deixar a tela aberta e porder fechar quando quiser
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
#mudanca