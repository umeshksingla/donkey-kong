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

for stair in board.allbStairs:
    hit = pygame.sprite.spritecollide(stair, board.allCoins, True)      # remove coins which are placed above stairs

possibilities = range(0,1000)
#print possibilities
#board.screen.blit(pygame.image.load(board.background),(0,0))
#the main controller
def main():
    pygame.init()
    clock=pygame.time.Clock()
    s=0
    # Loop that goes forever until exited manually
    while True:

        if board.game_over == True:

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()
            #print "yes game over"
            board.screen.fill(board.cream)
            hi = board.myFont.render(str("GAME OVER : "+str(living_beings.player.points)), 1, board.font_color)
            board.screen.blit(hi,(
                (board.screen_height - 2*board.border_width)/2 - 100,
                (board.screen_height - 2*board.border_width)/2
            ))
            pygame.display.update()
        else:
            s=0
            if possibilities[random.randint(0,999)]%200==0:
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

            if not living_beings.player.lives:
                board.game_over = True
            living_beings.player.draw()

            board.allbStairs.draw(board.screen)
            board.allSprites.draw(board.screen)
            board.allCoins.draw(board.screen)
            #board.playerSprite.draw(board.screen)

            clock.tick(60)

            pygame.display.update()
            #print person.sprites


if __name__ == "__main__":
    main()
