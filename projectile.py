import pygame
import math
class shoot(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.portee = 500
        self.player = player
        self.speed = 2
        self.image = pygame.image.load(
            "PygameAssets-main/projectile.png"
        )
        self.image = pygame.transform.scale(
            self.image,
            (50,50)
        )
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.origin = self.image
        self.angle=0
    def rotation(self):
        self.angle += 50
        self.image = pygame.transform.rotozoom(
            self.origin,
            self.angle,
            math.sin(8)
        )
        self.rect=self.image.get_rect(
            center=self.rect.center
        )

    def rightshot(self):
        self.rect.x += self.speed
        self.rotation()
        if math.sqrt((self.rect.y-self.player.rect.y)**2 + (self.rect.x-self.player.rect.x)**2) > self.portee:
            self.rightdelete()
    def leftshot(self):
        self.rect.x -= self.speed
        self.rotation()
        if math.sqrt((self.rect.y-self.player.rect.y)**2 +(self.rect.x-self.player.rect.x)**2) > self.portee:
            self.leftdelete()
    def leftdelete(self):
       self.player.shootingleft.remove(self)
    def rightdelete(self):
        self.player.shootingright.remove(self)


