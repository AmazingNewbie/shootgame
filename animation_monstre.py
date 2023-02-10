import pygame
class animation(pygame.sprite.Sprite):
    def __init__(self,spritename):
        super().__init__()
        self.image = pygame.image.load(f'PygameAssets-main/{spritename}.png')
def imagesload(spritename):
        path = f"PygameAssets-main/{spritename}/{spritename}"
        for num in range(1,24):
            path+num+".png"
