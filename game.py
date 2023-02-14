import pygame
from classe_joueur import joueur
from monster import monster
from cometfall import Cometfall
class Game:
    def __init__(self):
        self.playing = False
        self.players = pygame.sprite.Group()
        self.player = joueur(self)
        self.comets = Cometfall(self)
        self.players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
    def spawning(self):
        mob = mummy(self)
        self.all_monsters.add(mob)
    def collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    def over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.pv = 50
        self.playing = True
        self.spawning()
    def update(self,ecran):
        ecran.blit(self.player.image, self.player.rect)
        for e in self.player.shootingright:
            e.rightshot()
            self.player.event = True
        for t in self.player.shootingleft:
            t.leftshot()
            self.player.event = True
        for monster in self.all_monsters:
            monster.step()
            monster.update_health_bar(ecran)
            monster.update_animation()
        for comets in self.comets.cometsgroup:
            comets.falling()
        self.player.shootingright.draw(ecran)
        self.player.shootingleft.draw(ecran)
        self.all_monsters.draw(ecran)
        self.player.health_bar(ecran)
        self.comets.UpdateBar(ecran)
        if self.player.event:
            self.player.animate()
        self.comets.cometsgroup.draw(ecran)
        if self.pressed.get(pygame.K_d) and self.player.rect.x <= 2000:
            self.player.rigth()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y <= 1000:
            self.player.down()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x >= 0:
            self.player.left()
        elif self.pressed.get(pygame.K_z) and self.player.rect.y >= 0:
            self.player.up()




