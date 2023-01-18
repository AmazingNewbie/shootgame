import pygame
import random
class monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.pv=100
        self.pvlimit=100
        self.image=pygame.image.load(
            "PygameAssets-main/mummy.png"
        )
        self.rect=self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = random.randint(0, 750)
        self.strength = 5
        self.speed = 1
        self.game = game
    def step(self):
        if not self.game.collision(self,self.game.players):
            self.rect.x -= self.speed

