import pygame, sys, random
from pygame.locals import *

#modules
import coin, fireball, person
from layout import *

board = Board()                # initialise the board and screen
#allSprites = person.Sprites()  # initialise allSprites
living_beings = person.livingBeings()

coins = coin.drawCoins()
#the main controller
def main():
    pygame.init()
    clock=pygame.time.Clock()
    # Loop that goes forever until exited manually
    while True:
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

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    living_beings.player.changespeed(board.lefti)
                elif event.key == pygame.K_RIGHT:
                    living_beings.player.changespeed(board.righti)
                elif event.key == pygame.K_UP:
                    living_beings.player.changespeed(board.upi)
                elif event.key == pygame.K_DOWN:
                    living_beings.player.changespeed(board.downi)



        board.screen.fill(board.white)
        living_beings.player.handle_keys()
        living_beings.player.draw()
        board.allSprites.draw(board.screen)
        clock.tick(60)
        pygame.display.update()
        #print person.sprites


if __name__ == "__main__":
    main()
