import pygame
class animation(pygame.sprite.Sprite):
    def __init__(self,spritename):
        super().__init__()
        self.image = pygame.image.load(f'PygameAssets-main/{spritename}.png')
def imagesload(spritename):
        image=[]
        path = f"PygameAssets-main/{spritename}/{spritename}"
        for num in range(1,24):
            way=path+num+".png"
            image.append(pygame.image.load(way))
