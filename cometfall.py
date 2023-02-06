import pygame
from comet import meteorite
from  random import randint

class Cometfall:
    def __init__(self,game):
        self.prozent = 0
        self.cometsgroup = pygame.sprite.Group()
        self.game=game

    def event(self):
        self.cometsgroup.add(meteorite(self))

    def AddToProzent(self):
        self.prozent += 0.02

    def ResetProzent(self):
        self.prozent = 0

    def Plain(self):
        return self.prozent >= 10

    def ProzentComplete(self):
        if self.Plain():
            self.ResetProzent()
            self.event()

    def UpdateBar(self, surface):
        self.AddToProzent()
        self.ProzentComplete()
        bar_color = (250, 50, 50)
        bg_color = (4, 3, 2)
        bar_position = [20, 0, self.prozent * 100, 20]
        bg_position = [20, 0, 1000, 20]
        pygame.draw.rect(surface, bg_color, bg_position)
        pygame.draw.rect(surface, bar_color, bar_position)
