import pygame
class meteorite(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("PygameAssets-main/comet.png")
        self.rect = self.image.get_rect()