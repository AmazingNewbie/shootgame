import pygame
from projectile import shoot


class joueur(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pv = 50
        self.pvlimit = 150
        self.attack = 55
        self.speed = 1
        self.shootingright = pygame.sprite.Group()
        self.shootingleft = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 70

    def rigth(self):
        if not self.game.collision(self, self.game.all_monsters):
            self.rect.x += self.speed

    def left(self):
        self.rect.x -= self.speed

    def up(self):
        self.rect.y -= self.speed

    def down(self):
        self.rect.y += self.speed

    def tirerdroite(self):
        self.shootingright.add(shoot(self))

    def tirergauche(self):
        self.shootingleft.add(shoot(self))

    def health_bar(self, surface):
        color = (99, 111, 23)
        bar_position = [self.rect.x, self.rect.y, self.pv, 7]
        pygame.draw.rect(surface, color, bar_position)

    def damage(self, value):
        if self.pv >= 0:
            self.pv -= value
        else:
            self.game.playing = False
