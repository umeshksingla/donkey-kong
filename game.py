######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame, sys, random
from pygame.locals import *

#modules
import coin, fireball, person
from layout import *

board = Board()                # initialise the board and screen
#allSprites = person.Sprites()  # initialise allSprites
living_beings = person.livingBeings()

coins = coin.drawCoins()

#board.screen.blit(pygame.image.load(board.background),(0,0))
#the main controller
def main():
    pygame.init()
    clock=pygame.time.Clock()
    s=0
    # Loop that goes forever until exited manually
    while True:
        s=0
        if living_beings.donkey.rect.x % random.randint(25,50) == 43:
            s = 1
            #print "fire..."
            fireBall = fireball.drawFireball()
            board.allFireballs.add(fireBall)
            board.allSprites.add(fireBall)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    living_beings.player.changespeed(board.left)
                elif event.key == pygame.K_RIGHT:
                    living_beings.player.changespeed(board.right)
                elif event.key == pygame.K_UP:
                    living_beings.player.changespeed(board.up)
                elif event.key == pygame.K_DOWN:
                    living_beings.player.changespeed(board.down)
                elif event.key == pygame.K_SPACE:
                    living_beings.player.jump()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    living_beings.player.changespeed(board.lefti)
                elif event.key == pygame.K_RIGHT:
                    living_beings.player.changespeed(board.righti)
                elif event.key == pygame.K_UP:
                    living_beings.player.movey = 0
                elif event.key == pygame.K_DOWN:
                    living_beings.player.movey = 0


        board.screen.fill(board.cream)

        living_beings.player.handle_keys()
        living_beings.donkey.handle_keys()

        for fireb in board.allFireballs:
            fireb.handle_keys()

        living_beings.player.draw()

        board.allbStairs.draw(board.screen)
        board.allSprites.draw(board.screen)
        board.allCoins.draw(board.screen)
        board.playerSprite.draw(board.screen)

        clock.tick(60)
        pygame.display.update()
        #print person.sprites


if __name__ == "__main__":
    main()
