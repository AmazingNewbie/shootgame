import pygame
from random import randint
class meteorite(pygame.sprite.Sprite):
    def __init__(self,fall):
        super().__init__()
        self.image = pygame.image.load("PygameAssets-main/comet.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(20,500)
        self.speed = randint(1,3)
        self.comet= fall
    def delete(self):
        self.comet.cometsgroup.remove(self)
    def falling(self):
        if self.rect.y< 600:
            self.rect.y += self.speed
        else:
            self.delete()
        if self.comet.game.collision(self,self.comet.game.players):
            self.delete()
            self.comet.game.player.damage(5)

