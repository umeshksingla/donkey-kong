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

    def checkWall(self):
        pass

    def handle_keys(self):
        pass



class Donkey(Person):

    def handle_keys(self):

        allHits = pygame.sprite.spritecollide(self, board.allBlocks, False)

        #print allHits, "1"

        if len(allHits)>0:
            self.movex = -1*self.movex

        self.rect.x += self.movex

        allHits = pygame.sprite.spritecollide(self, board.playerSprite, False)

        #print allHits, "2"

        if len(allHits):
            pygame.quit()
            sys.exit()


class Player(Person):

    lives = 3

    def changespeed(self, coor):
        #print coor
        self.movex += coor[0]
        self.movey += coor[1]

    def handle_keys(self):


        #check whether player is colliding with stairs
        #self.rect.y+=5
        allHits = pygame.sprite.spritecollide(self, board.allStairs, False)
        #self.rect.y-=5

        if len(allHits) > 0:
            if self.movey > 2:
                self.movey=0
            self.onstair = True
        else:
            self.onstair = False

        #print self.onstair



        self.stickBelow()

        #left and right moves
        self.rect.x += self.movex

        #check collisions for right and left
        allHits = pygame.sprite.spritecollide(self, board.allBlocks, False)

        for hit in allHits:
            if self.movex > 0:
                self.rect.right = hit.rect.left
            elif self.movex < 0:
                self.rect.left = hit.rect.right


        #up and down moves
        self.rect.y += self.movey

        # check collisions for up and down
        allHits = pygame.sprite.spritecollide(self, board.allBlocks, False)

        for hit in allHits:
            if self.movey > 0:
                self.rect.bottom = hit.rect.top
            elif self.movey < 0:
                self.rect.top = hit.rect.bottom
            self.movey = 0

        #position
        self.position = board.myFont.render(str("P Position : " + str(self.rect.x)+" , "+str(self.rect.y)+" , "+str(self.movex)+" , " + str(self.movey)), 1, board.blue)

        # check collisions with the coins
        coinHits = pygame.sprite.spritecollide( self, board.allCoins, True)

        for hit in coinHits:
            self.points += 10

        # check collisions with the fireballs
        fireHits = pygame.sprite.spritecollide( self, board.allFireballs, False)

        if len(fireHits):
            self.lives -= 1
            self.points -= 50
            self.rect.x = board.border_width+1
            self.rect.y = board.screen_height - 8*board.border_width
            #self.movex=0
            #self.movey=0

        #score
        self.score = board.myFont.render(str("Score : "+str(self.points)), 1, board.font_color)

        #lives
        self.life = board.myFont.render(str("Lives : "+str(self.lives)), 1, board.font_color)

        if not self.lives:
            pygame.quit()
            sys.exit()

    def jump(self):
        if not self.onstair:
            self.rect.y += 2
            allHits = pygame.sprite.spritecollide(self,board.allBlocks,False)
            self.rect.y -= 2

            if len(allHits) > 0 or self.rect.bottom >= board.screen_height - 3*board.border_width:
                self.movey = -7

        #print "allHits", allHits, self.movey

    def stickBelow(self):
        if not self.onstair:
            if self.movey == 0:         # when player falls off a platform freely
                self.movey = 1
            else:
                self.movey += board.acc_val
        # if self.rect.y >= board.screen_height - 3*board.border_width - self.rect.height and self.movey >= 0:
        #     self.movey = 0
        #     self.rect.y = board.screen_height - 3*board.border_width - self.rect.height

    def stop(self):
        self.movey = 0

    def getPosition(self):
        return self.position

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
        3*board.border_width,
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
     stair = Donkey("stair", 370, 5.5*board.gap-5, board.ladder, 40, board.gap+10, 0)
     board.allStairs.add(stair)
     board.allSprites.add(stair)
     # princess instance
     #print princess
     board.playerSprite.add(player)
     board.allSprites.add(donkey)
     board.allSprites.add(princess)
