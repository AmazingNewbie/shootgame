import pygame
from classe_joueur import joueur
from monster import monster
class Game:
    def __init__(self):
        self.playing = False
        self.players = pygame.sprite.Group()
        self.player = joueur(self)
        self.players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawning()
    def spawning(self):
        mob = monster(self)
        self.all_monsters.add(mob)
    def collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    def update(self,ecran):
        ecran.blit(self.player.image, self.player.rect)
        for e in self.player.shootingright:
            e.rightshot()
        for t in self.player.shootingleft:
            t.leftshot()
        for monster in self.all_monsters:
            monster.step()
            monster.update_health_bar(ecran)
        self.player.shootingright.draw(ecran)
        self.player.shootingleft.draw(ecran)
        self.all_monsters.draw(ecran)
        self.player.health_bar(ecran)

        if self.pressed.get(pygame.K_d) and self.player.rect.x <= 2000:
            self.player.rigth()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y <= 1000:
            self.player.down()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x >= 0:
            self.player.left()
        elif self.pressed.get(pygame.K_z) and self.player.rect.y >= 0:
            self.player.up()




