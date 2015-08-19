######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame, layout, person, time, random, sys
from pygame.locals import *

board = layout.Board()


class drawFireball(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.movex = 1
        self.movey = 0

        self.posx = person.livingBeings.donkey.rect.x
        self.posy = person.livingBeings.donkey.rect.y + person.livingBeings.donkey.rect.height - 3*board.border_width

        self.image = pygame.image.load(board.fireball).convert_alpha()
        self.image = pygame.transform.scale(self.image,( 3*board.border_width - 20, 3*board.border_width - 20))
        self.width = 3*board.border_width-20
        self.height = 3*board.border_width-20

        self.rect = self.image.get_rect()
        self.rect.x = self.posx;
        self.rect.y = self.posy;

        #     fireBall = Fireball(person.livingBeings.donkey.rect.x, person.livingBeings.donkey.rect.y)


    def moveH(self):

        self.rect.x += self.movex
        allHits = pygame.sprite.spritecollide(self, board.allBorders, False)

        for hit in allHits:
            if self.movex > 0:
                self.rect.right = hit.rect.left
            elif self.movex < 0:
                self.rect.left = hit.rect.right
            self.movex*=-1


    def handle_keys(self):

        self.moveH()
        self.stickBelow()

        #print self.rect.x , self.rect.y

        self.rect.y += self.movey

        # check collisions for up and down
        allHits = pygame.sprite.spritecollide(self, board.allBlocks, False)

        for hit in allHits:
            if self.movey > 0:
                self.rect.bottom = hit.rect.top
            elif self.movey < 0:
                self.rect.top = hit.rect.bottom
            self.movey = 0

        # allHits = pygame.sprite.spritecollide(self, board.playerSprite, False)
        #
        # #print allHits, "2"
        #
        # if len(allHits):
        #     pygame.quit()
        #     sys.exit()

    def stickBelow(self):
        if self.movey == 0:         # when player falls off a platform freely
            self.movey = 1
        else:
            self.movey += board.acc_val_fireball
        #print self.movex, self.movey
