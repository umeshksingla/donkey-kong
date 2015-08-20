######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame
import level
import layout, person, time, random, sys
from pygame.locals import *

board = layout.Board()

class drawFireball(pygame.sprite.Sprite):

    def __init__(self, donkey_x, donkey_y, donkey_height):

        pygame.sprite.Sprite.__init__(self)

        self.movex = 1
        self.movey = 0

        self.chooseToDrop = 1

        #hi = person.livingBeings()
        self.posx = donkey_x
        self.posy = donkey_y + donkey_height - 3*board.border_width

        self.image = pygame.image.load(board.fireball).convert_alpha()
        self.image = pygame.transform.scale(self.image,( 3*board.border_width - 20, 3*board.border_width - 20))
        self.width = 3*board.border_width-20
        self.height = 3*board.border_width-20

        self.rect = self.image.get_rect()
        self.rect.x = self.posx;
        self.rect.y = self.posy;

    def checkCollisions(self, withWhom, disappear):

        return pygame.sprite.spritecollide(self, withWhom, disappear)
        #     fireBall = Fireball(person.livingBeings.donkey.rect.x, person.livingBeings.donkey.rect.y)


    def __moveHorizontally(self):

        if self.rect.x <= board.border_width + 2 and self.rect.y >= board.screen_height - 3*board.border_width - self.height:
            board.allFireballs.remove(self)     #remove from fireballs list
            board.allSprites.remove(self)       #remove from all sprites list also


        self.rect.x += self.movex
        allHits = self.checkCollisions(board.allBorders, False)

        for hit in allHits:
            if self.movex > 0:
                self.rect.right = hit.rect.left
            elif self.movex < 0:
                self.rect.left = hit.rect.right
            self.movex*=-1



    def handle_keys(self):

        self.__moveHorizontally()

        allHits =  self.checkCollisions(board.allbStairs, False)

        self.chooseToDrop = random.choice([0,0,0,1,1,1,1])

        self.__stickBelow()

        #print self.rect.x , self.rect.y

        self.rect.y += self.movey

        # check collisions for up and down
        #print board.allbBlocks

        allHits = self.checkCollisions(board.allbBlocks, False)

        for hit in allHits:
            if self.movey > 0:
                self.rect.bottom = hit.rect.top
            elif self.movey < 0:
                self.rect.top = hit.rect.bottom
            self.movey = 0


    def __stickBelow(self):
        if self.chooseToDrop:
            if self.movey == 0:         # when player falls off a platform freely
                self.movey = 1
            else:
                self.movey += board.acc_val_fireball
            #print self.movex, self.movey
