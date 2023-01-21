
import pygame
from game import Game
pygame.init()
pygame.display.set_caption("manger")
ecran = pygame.display.set_mode((1500, 633))
running = True
background = pygame.image.load(
    'PygameAssets-main/bg.jpg'
)
background = pygame.transform.scale(background,(1500,633))
game = Game()
while running:
    ecran.blit(background, (0, 0))


    