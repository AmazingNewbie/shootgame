import pygame
from classe_joueur import joueur
from monster import monster
class Game:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.player = joueur(self)
        self.players.add(self.player)
        self.pressed = {}
        self.spawning()
    def spawning(self):
        mob=monster()
        self.all_monsters.add(
            mob
        )
    def collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
