import pygame

WIDTH = 800
pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
pygame.quit()