import pygame
import random
import animation_monstre

class monster(animation_monstre.animation):
    def __init__(self, game,name,size):
        super().__init__(name,size)
        self.pv = 100
        self.pvlimit = 100
        self.rect = self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = random.randint(0, 600)
        self.strength = 1
        self.speed = 1
        self.game = game
        self.name = name

    def step(self):
        if not self.game.collision(self, self.game.players):
            self.rect.x -= self.speed
            self.respawn()
        else:
            self.game.player.damage(self.strength)



    def update_health_bar(self, surface):
        bar_color = (5, 88, 6)
        colorbg = (77, 55, 77)
        bar_position = [self.rect.x, self.rect.y - 5, self.pv, 5]
        bgposition = [self.rect.x, self.rect.y - 5, self.pvlimit, 5]
        pygame.draw.rect(surface, colorbg, bgposition)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
        self.pv -= amount
        self.respawn()
    def respawn(self):
        if self.pv <= 0 or self.rect.x<=0:
            self.game.all_monsters.remove(self)
            self.game.comets.ProzentComplete()
            if not self.game.comets.Plain():
                self.game.spawning(mummy)

    def update_animation(self):
        self.animation()
class mummy(monster):
    def __init__(self,game):
        super().__init__(game,"mummy",(130,130))
class Alien(monster):
    def __init__(self,game):
        super().__init__(game,"alien",(300,300))

