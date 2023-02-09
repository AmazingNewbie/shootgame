import pygame
from game import Game

pygame.init()
pygame.display.set_caption("manger")
ecran = pygame.display.set_mode((1500, 633))
running = True
menu = pygame.image.load("PygameAssets-main/banner.png")
menu = pygame.transform.scale(menu, (500, 500))
menurect = menu.get_rect()
menurect.x = 500
menurect.y = 67
button = pygame.image.load('PygameAssets-main/button.png')
button = pygame.transform.scale(button, (400, 150))
button_rect = button.get_rect()
button_rect.x = 550
button_rect.y = 450
background = pygame.image.load('PygameAssets-main/bg.jpg')
background = pygame.transform.scale(background, (1500, 633))
game = Game()
while running:

    ecran.blit(background, (0, 0))
    if game.playing:
        game.update(ecran)
    elif not game.playing:
        ecran.blit(menu, menurect)
        ecran.blit(button, button_rect)
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            game.pressed[i.key] = True
            if i.key == pygame.K_RIGHT:
                game.player.tirerdroite()
            elif i.key == pygame.K_LEFT:
                game.player.tirergauche()
        elif i.type == pygame.KEYUP:
            game.pressed[i.key] = False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(i.pos):
                game.over()
        print(game.comets.cometsgroup)
