
import pygame
from game import Game
pygame.init()
pygame.display.set_caption("manger")
ecran = pygame.display.set_mode((1500, 633))
running = True
background = pygame.image.load(
    'PygameAssets-main/bg.jpg'
)
background = pygame.transform.scale(background,(1500,633))
game = Game()
while running:
    ecran.blit(background, (0, 0))
    if game.playing:
        ecran.blit(game.player.image, game.player.rect)
        for e in game.player.shootingright:
            e.rightshot()

        for t in game.player.shootingleft:
            t.leftshot()
        for monster in game.all_monsters:
            monster.step()
            monster.update_health_bar(ecran)
        game.player.shootingright.draw(ecran)
        game.player.shootingleft.draw(ecran)
        game.all_monsters.draw(ecran)
        game.player.health_bar(ecran)
        pygame.display.flip()
        if game.pressed.get(pygame.K_d) and game.player.rect.x <= 2000:
            game.player.rigth()
        elif game.pressed.get(pygame.K_s) and game.player.rect.y <= 1000:
            game.player.down()
        elif game.pressed.get(pygame.K_q) and game.player.rect.x >= 0:
            game.player.left()
        elif game.pressed.get(pygame.K_z) and game.player.rect.y >= 0:
            game.player.up()



        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running=False
                pygame.quit()
            elif i.type == pygame.KEYDOWN:
                game.pressed[i.key] = True
                if i.key == pygame.K_RIGHT:
                    game.player.tirerdroite()
                elif i.key == pygame.K_LEFT:
                    game.player.tirergauche()
            elif i.type == pygame.KEYUP:
                game.pressed[i.key] = False

    