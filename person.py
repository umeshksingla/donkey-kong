import pygame, layout, sys
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



class Donkey(Person):
    def update(self):
        pass



class Player(Person):
    # def handle_keys(self):
    #
    #     key = pygame.key.get_pressed()
    #     #print key
    #     if key[pygame.K_UP]:
    #         if self.onStair():
    #             self.movey=-1
    #             self.rect.y+=self.movey
    #             #print "up stair"
    #         else:
    #             #print "inside else"
    #             self.stickBelow()
    #     else:
    #         #print "outside else"
    #         self.stickBelow()
    #
    #     # right and left side moves
    #     if not self.checkWall():
    #
    #         if key[pygame.K_RIGHT]: # right key
    #             self.rect = self.rect.move(board.right) # move right
    #             self.movex=2
    #
    #         elif key[pygame.K_LEFT]: # left key
    #             self.rect = self.rect.move(board.left) # move left
    #             self.movex=-2
    #
    #         elif key[pygame.K_SPACE] and not self.onStair(): # space key
    #             self.jump()
    #
    #     if key[pygame.K_DOWN]:
    #         #print "down button"
    #         self.rect.y+=5
    #         allHits=pygame.sprite.spritecollide(self,board.allStairs,False)
    #         self.rect.y-=5
    #         for hit in allHits:
    #             self.rect.bottom=hit.rect.bottom
    #             #pygame.time.delay(5)
    #
    #
    #     # up and down moves
    #     self.rect.y += self.movey
    #
    #     allHits = pygame.sprite.spritecollide( self, board.allBlocks, False)
    #
    #     for hit in allHits:
    #         if self.movey > 0 or self.onstair:
    #             self.onstair=False
    #             self.rect.bottom = hit.rect.top
    #         elif self.movey<0:
    #             self.rect.top = hit.rect.bottom
    #             #self.onstair=False
    #         self.movey=0
    #
    #
    # def stickBelow(self):       # when player falls from above floor
    #
    #     #when we are on ground only and up button is pressed
    #     if self.rect.y >= board.screen_height-6*board.border_width and self.movey>=0:
    #         self.movey=0
    #         self.rect.y = board.screen_height - 6*board.border_width
    #
    #     #when we are falling from upper level
    #     if self.movey==0: # not moving in y direction
    #         self.movey=1
    #     else:
    #         self.movey+=0.25    #accelerate: add 0.25 to 1 every time
    #
    # def jump(self):
    #
    #     self.rect.y+=2
    #     allHits = pygame.sprite.spritecollide(self, board.allBlocks, False)
    #     self.rect.y-=2
    #     if len(allHits) > 0:
    #         self.movey=-5
    #
    # def onStair(self):
    #     allHits=pygame.sprite.spritecollide(self, board.allStairs, False)
    #     if len(allHits):
    #         self.onstair=True
    #         #print "stair"
    #         return True
    #     return False
##########################################################################33
    def changespeed(self, coor):
        self.movex += coor[0]
        self.movey += coor[1]

    def handle_keys(self):

        self.stickBelow()

        #left and right moves
        self.rect.x += self.movex   #movex defined by

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
        #posiiton
        self.position = board.myFont.render(str("P Position : " + str(self.rect.x)+" , "+str(self.rect.y)+" , "+str(self.movex)+" , " + str(self.movey)), 1, board.blue)


        # check collisions with the coins
        coinHits = pygame.sprite.spritecollide( self, board.allCoins, True)

        for hit in coinHits:
            self.points += 10
        #score
        self.score = board.myFont.render(str("Score : "+str(self.points)), 1, board.blue)

    def stickBelow(self):

        if self.movey == 0:
            self.movey = 1
        else:
            self.movey += board.acc_val

        if self.rect.y >= board.screen_height - 3*board.border_width - self.rect.height and self.movey >= 0:
            self.movey = 0
            self.rect.y = board.screen_height - 3*board.border_width - self.rect.height

    def getPosition(self):
        return self.position

    def getScore(self):
        return self.score

    def draw(self):
        board.screen.blit(self.getPosition(),(board.screen_width - 24 * board.border_width - 50, board.screen_height - 2*board.border_width))
        board.screen.blit(self.getScore(),(4*board.border_width , board.screen_height - 2*board.border_width))

class livingBeings(object):
     #living beings
     player = Player("UMESH",
        board.border_width+1,
        board.screen_height-8*board.border_width,
        board.mario,
        3*board.border_width,
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
     stair = Donkey("stair",370,5.5*board.gap,board.ladder,40,board.gap,0)
     board.allStairs.add(stair)
     board.allSprites.add(stair)
     # princess instance
     #print princess
     board.allSprites.add(player)
     board.allSprites.add(donkey)
     board.allSprites.add(princess)
