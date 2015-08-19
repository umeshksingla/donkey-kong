######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame, layout, sys, random
from pygame.locals import *

class Sprites():
    allSprites = pygame.sprite.Group()

board = layout.Board()

player = None
donkey = None
princess = None

class Person(pygame.sprite.Sprite):

    def __init__(self, name, startx, starty, image, image_width, image_height, points):
        pygame.sprite.Sprite.__init__(self)

        self.name = name

        self.posx = startx
        self.posy = starty
        self.movex = 0
        self.movey = 0

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(image_width,image_height))
        self.rect = self.image.get_rect()
        self.rect.x = startx;
        self.rect.y = starty;

        self.onstair=False
        self.points = points
        #self.position = layout.myFont.render(str("P Position : " + str(self.posx)+" , "+str(self.posy)), 1, blue)

    def checkCollisions(self, withWhom, disappear):

        return pygame.sprite.spritecollide(self, withWhom, disappear)

    def handle_keys(self):
        pass


class Donkey(Person):

    def handle_keys(self):

        allHits = self.checkCollisions(board.allBlocks, False)

        #print allHits, "1"

        if len(allHits)>0:
            self.movex = -1*self.movex

        self.rect.x += self.movex

        if self.rect.x >= 440 - 2*board.border_width:
            self.movex = -1*self.movex
        #allHits = self.checkCollisions(board.playerSprite, False)

        #print allHits, "2"

        #if len(allHits):
        #    pygame.quit()
        #    sys.exit()


class Player(Person):

    lives = 3

    def changespeed(self, coor):
        #print coor
        self.movex += coor[0]
        self.movey += coor[1]

    def handle_keys(self):

        #check whether player is colliding with stairs
        #self.rect.y+=5
        allHits = self.checkCollisions(board.allStairs, False)
        #self.rect.y-=5

        if len(allHits) > 0:
            if self.movey > 2:
                self.movey=0
            self.onstair = True
        else:
            self.onstair = False
        #print self.onstair

        #gravity acting all the time except when on stair
        self.stickBelow()

        #left and right moves
        self.rect.x += self.movex

        #check collisions for right and left
        self.checkHor()

        #up and down moves
        self.rect.y += self.movey

        # check collisions for up and down
        self.checkVer()

        # check collisions with the coins
        self.collectCoins()

        # check collisions with the fireballs
        self.hitFireballs()

        # check colliison with the princess
        hitPrincess = self.checkCollisions(board.princessSprite, False)

        for hit in hitPrincess:
            self.points += 50
            #board.reload()

        #score
        self.score = board.myFont.render(str("Score : "+str(self.points)), 1, board.font_color)

        #lives
        self.life = board.myFont.render(str("Lives : "+str(self.lives)), 1, board.font_color)

        if self.lives==0:
            board.game_over = True
            #pygame.quit()
            #sys.exit()

    def checkHor(self):
        allHits = self.checkCollisions(board.allBlocks, False)

        for hit in allHits:
            if self.movex > 0:
                self.rect.right = hit.rect.left
            elif self.movex < 0:
                self.rect.left = hit.rect.right

    def checkVer(self):
        allHits = self.checkCollisions( board.allBlocks, False)

        for hit in allHits:
            if self.movey > 0:
                self.rect.bottom = hit.rect.top
            elif self.movey < 0:
                self.rect.top = hit.rect.bottom
            self.movey = 0

    def jump(self):
        if not self.onstair:    # disable jump on stair
            self.rect.y += 2
            allHits = self.checkCollisions(board.allBlocks, False)
            self.rect.y -= 2

            if len(allHits) > 0 or self.rect.bottom >= board.screen_height - 3*board.border_width:
                self.movey = -5

        #print "allHits", allHits, self.movey

    def stickBelow(self):
        if not self.onstair:            # disable gravity on stair
            if self.movey == 0:         # when player falls off a platform freely
                self.movey = 1
            else:
                self.movey += board.acc_val     # increase speed as it goes down

        # if self.rect.y >= board.screen_height - 3*board.border_width - self.rect.height and self.movey >= 0:
        #     self.movey = 0
        #     self.rect.y = board.screen_height - 3*board.border_width - self.rect.height

    def stop(self):
        self.movey = 0

    def collectCoins(self):
        coinHits = self.checkCollisions(board.allCoins, True)

        for hit in coinHits:
            self.points += 5

    def hitFireballs(self):
        fireHits = self.checkCollisions( board.allFireballs, True)

        if len(fireHits):
            self.lives -= 1                     # decrease life by 1
            self.points -= 25
            if self.points < 0:                # decrease points by 20
                self.points = 0
            self.rect.x = board.border_width+1  # player goes to initial position
            self.rect.y = board.screen_height - 8*board.border_width
            #self.movex=0
            #self.movey=0
            #for fireb in board.allFireballs:
            #    board.allFireballs.remove(fireb)

    def getPosition(self):
        return board.myFont.render(str("P Position : " + str(self.rect.x)+" , "+str(self.rect.y), 1, board.blue))

    def getScore(self):
        return self.score

    def draw(self):
        #board.screen.blit(self.getPosition(),(board.screen_width - 24 * board.border_width - 50, board.screen_height - 2*board.border_width))
        board.screen.blit(self.getScore(),(4*board.border_width , board.screen_height - 2*board.border_width))
        board.screen.blit(self.life,(board.screen_width - 24 * board.border_width - 50 , board.screen_height - 2*board.border_width))

class livingBeings(object):
     #living beings
     player = Player("UMESH",
        board.border_width+1,
        board.screen_height-8*board.border_width,
        board.mario,
        3*board.border_width-10,
        3*board.border_width-10,
        0
        ) # player instance

     donkey = Donkey(
        "DONKEY",
        board.border_width+1,
        board.gap,
        board.donkey,
        4*board.border_width,
        4*board.border_width,
        0
        )
     donkey.movex = 3
     # donkey instance
     #print princess
     princess = Player(
        "PRINCESS",
        120,
        board.border_width,
        board.princess,
        2*board.border_width,
        4*board.border_width,
        0
        )
     # princess instance

     #print princess
     board.princessSprite.add(princess)
     board.allSprites.add(donkey)
     board.allSprites.add(princess)
     board.allSprites.add(player)
