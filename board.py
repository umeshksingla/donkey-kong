######## Aug 20, 2015 ########
######## Umesh Singla ########

import pygame, sys, random
from pygame.locals import *

#modules
import coin, fireball, person
from layout import *

class Game(object):

    def __init__(self):

        self.board = Board()                # initialise the board and screen
        #allSprites = person.Sprites()  # initialise allSprites
        self.living_beings = person.livingBeings()
        self.coins = coin.drawCoins()

        self.stairs = Stairs()
        self.borders = Borders()
        self.bstairs = BrokenStairs()
        self.platforms = Platforms()

        for stair in self.board.allbStairs:
            hit = pygame.sprite.spritecollide(stair, self.board.allCoins, True)      # remove coins which are placed above stairs

    def drawStartScreen(self):
        c=0
        for i in ["'A' TO MOVE LEFT","'D' TO MOVE RIGHT","'W' TO MOVE UP","'S' TO MOVE DOWN","'SPACE' TO JUMP","'Q' TO QUIT"]:
            startText = self.board.myFont.render(i, 1, self.board.font_color)
            self.board.screen.blit(startText,( self.board.startFontx, self.board.startFonty+3*c*self.board.border_width))
            c+=1

        startText = self.board.myFont.render(str("PRESS 'S' TO START"), 1, self.board.dark_brown)
        self.board.screen.blit( startText,( self.board.startFontx, self.board.startFonty + 400))

    def drawGameOverScreen(self, playerScore):

        startText = self.board.myFont.render("GAME OVER", 1, self.board.font_color)
        self.board.screen.blit(startText,(self.board.startFontx+50,self.board.startFonty))

        startText = self.board.myFont.render(str("SCORE : "+str(playerScore)), 1, self.board.red)
        self.board.screen.blit(startText,(self.board.startFontx,self.board.startFonty+6*self.board.border_width))

        startText = self.board.myFont.render(str("PRESS 'R' TO RESTART"), 1, self.board.dark_brown)
        self.board.screen.blit( startText,(self.board.startFontx,self.board.startFonty + 400))

    def emptyTheSprites(self):

        self.board.allSprites.empty()
        self.board.allbStairs.empty()
        self.board.allBlocks.empty()
        self.board.allbBlocks.empty()
        self.board.allBorders.empty()
        self.board.allStairs.empty()
        self.board.allCoins.empty()
        self.board.allFireballs.empty()
        self.board.princessSprite.empty()
