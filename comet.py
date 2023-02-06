import pygame
class meteorite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PygameAssets-main/comet.png")
        self.rect = self.image.get_rect()
        self.speed =5
    def falling(self):
        self.rect.y += self.speed