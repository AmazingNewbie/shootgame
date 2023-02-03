import pygame
class Comet:
    def __init__(self):
        self.prozent = 0
    def AddToProzent(self):
        self.prozent += 2
    def UpdateBar(self,surface):
        bar_color = (100,0,0)
        bg_color= (4,3,2)
        bar_position = [20,0,self.prozent,10]
        bg_position= [20,0,100,10]
        pygame.draw.rect(surface,bg_color,bg_position)
        pygame.draw.rect(surface,bar_color,bar_position)
