######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame, sys, random
from pygame.locals import *

#modules
import coin, fireball, person
from layout import *
from board import *

#board.screen.blit(pygame.image.load(board.background),(0,0))
#the main controller
def main():
    pygame.init()
    clock=pygame.time.Clock()
    s=0
    start = False
    # Loop that goes forever until exited manually

    game = Game()

    board = game.board
    coins = game.coins
    living_beings = game.living_beings
    possibilities = range(0,1000)

    #print possibilities
    while True:

        if not start:

            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_s:
                    start = True
                    board.game_over = False
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()

            #print "yes game over"
            board.screen.fill(board.cream)

            game.drawStartScreen()

            pygame.display.update()

        elif board.game_over == True:

            board.screen.fill(board.cream)

            game.drawGameOverScreen(living_beings.player.points)

            past_score = living_beings.player.points

            for event in pygame.event.get():

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_r:

                    game.emptyTheSprites()

                    board.game_over = False
                    start = False

                    Game.__init__(game)     #initialize game again

                    board = game.board
                    coins = game.coins
                    living_beings = game.living_beings

                    living_beings.player.points = past_score
                    #print "initialize again", board.game_over

            pygame.display.update()

        else:
            s=0
            if possibilities[random.randint(0,999)]%200==0:
                s = 1
                #print "fire..."
                fireBall = fireball.drawFireball(
                    living_beings.donkey.rect.x,
                    living_beings.donkey.rect.y,
                    living_beings.donkey.rect.height )
                board.allFireballs.add(fireBall)
                board.allSprites.add(fireBall)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        living_beings.player.changespeed(board.left)
                    elif event.key == pygame.K_d:
                        living_beings.player.changespeed(board.right)
                    elif event.key == pygame.K_w:
                        living_beings.player.changespeed(board.up)
                    elif event.key == pygame.K_s:
                        living_beings.player.changespeed(board.down)
                    elif event.key == pygame.K_SPACE:
                        living_beings.player.jump()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        living_beings.player.changespeed(board.lefti)
                    elif event.key == pygame.K_d:
                        living_beings.player.changespeed(board.righti)
                    elif event.key == pygame.K_w:
                        living_beings.player.movey = 0
                    elif event.key == pygame.K_s:
                        living_beings.player.movey = 0


            board.screen.fill(board.cream)

            living_beings.player.handle_keys()
            living_beings.donkey.handle_keys()

            for fireb in board.allFireballs:
                fireb.handle_keys()

            if not living_beings.player.lives:
                board.game_over = True
                living_beings.player.points = 0

            if pygame.sprite.collide_rect(living_beings.player, living_beings.princess):
                board.game_over = True

            living_beings.player.draw()

            board.allSprites.draw(board.screen)
            board.allbStairs.draw(board.screen)
            board.allCoins.draw(board.screen)
            #board.playerSprite.draw(board.screen)

            clock.tick(60)

            pygame.display.update()
            #print person.sprites


if __name__ == "__main__":
    main()
