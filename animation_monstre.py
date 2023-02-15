import pygame
class animation(pygame.sprite.Sprite):
    def __init__(self,spritename, size=(200,200)):
        super().__init__()
        self.image = pygame.image.load(f'PygameAssets-main/{spritename}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0
        self.images= animations.get(spritename)
        self.event = False
    def animation(self):
        self.current_image +=1
        if self.current_image >= len(self.images):
            self.current_image = 0
            self.event= False
        self.image = self.images[self.current_image]
def imagesload(spritename):
        image=[]
        path = f"PygameAssets-main/{spritename}/{spritename}"
        for num in range(1,24):
            way=path+str(num)+".png"
            image.append(pygame.image.load(way))
        return image
animations={
    'mummy': imagesload('mummy'),
    'player': imagesload('player'),
    'alien': imagesload('alien')
}
