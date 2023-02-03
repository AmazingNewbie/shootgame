import pygame


class Cometfall:
    def __init__(self):
        self.prozent = 0

    def AddToProzent(self):
        self.prozent += 0.002

    def UpdateBar(self, surface):
        self.AddToProzent()
        bar_color = (100, 30, self.prozent*10)
        bg_color = (4, 3, 2)
        bar_position = [20, 0, self.prozent * 100, 20]
        bg_position = [20, 0, 10000, 20]
        pygame.draw.rect(surface, bg_color, bg_position)
        pygame.draw.rect(surface, bar_color, bar_position)
