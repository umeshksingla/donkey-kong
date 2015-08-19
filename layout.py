######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame
from pygame.locals import *

pygame.init()       #initialise pygame to initialise pygame.font and others

class Board(object):

    #screen dimensions
    screen_height = 690
    screen_width = 640
    border_width = 12
    gap = 100

    #fonts
    myFont = pygame.font.SysFont("Times New Roman", 2*border_width)

    #colors
    blue = (140,130,240)
    red = (255,0,0)
    green = (0,255,0)
    white = (255,255,255)
    black = (0,0,0)
    dark_brown = (53,40,31)
    brown = (142,91,60)
    cream = (255,253,208)
    font_color = (153,87,35)

    #speed and accelerate constants
    up , down, left, right = (0,-2),(0,2),(-2,0),(2,0)
    upi , downi, lefti, righti = (0,0),(0,0),(2,0),(-2,0)
    acc_val = 0.25
    acc_val_fireball = 0.15

    #display
    screen=pygame.display.set_mode((screen_width,screen_height),0,32)   #set the screen
    pygame.display.set_caption('Donkey Kong Game')

    #images
    mario = "mario.png"
    donkey = "donkey.png"
    princess = "princess.png"
    fireball = "fireball.png"
    coin = "coin.png"
    ladder = "ladder.png"
    background = "back.png"

    #sprites
    allBorders = pygame.sprite.Group()
    allStairs = pygame.sprite.Group()
    allbStairs = pygame.sprite.Group()
    allBlocks = pygame.sprite.Group()
    allbBlocks = pygame.sprite.Group()
    allCoins = pygame.sprite.Group()
    allFireballs = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()  #except player
    playerSprite = pygame.sprite.Group()

class drawRect(pygame.sprite.Sprite):

    def __init__(self,posx,posy,width,height,color):

        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

class drawStair(pygame.sprite.Sprite):

    def __init__(self, startx, starty, image, image_width, image_height):
        pygame.sprite.Sprite.__init__(self)

        self.posx = startx
        self.posy = starty

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(image_width,image_height))

        self.rect = self.image.get_rect()
        self.rect.x = startx;
        self.rect.y = starty;

board = Board()
class Borders(object):

    #creating borders and storing its instance in borders
    for i in [(0,0),(0,board.screen_height-3*board.border_width)]:
        border = drawRect(i[0], i[1], board.screen_width, board.border_width, board.dark_brown) #top
        board.allSprites.add(border)
        board.allBlocks.add(border)
        board.allBorders.add(border)

    for i in [(0,0),(board.screen_width - board.border_width,0)]:
        border = drawRect(i[0], i[1], board.border_width, board.screen_height, board.dark_brown) #top
        board.allSprites.add(border)
        board.allBlocks.add(border)
        board.allBorders.add(border)

class Platforms(object):

    #creating blocks
    block= drawRect(100,board.gap-50,200, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    block = drawRect(10,1.5*board.gap,350, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)
    block = drawRect(50+350,1.5*board.gap,40, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    block = drawRect(180,2.5*board.gap,60, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)
    block = drawRect(180+100,2.5*board.gap,120, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)
    block = drawRect(180+100+120+40,2.5*board.gap,190, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    block = drawRect(10,3.5*board.gap,440, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)
    block = drawRect(490,3.5*board.gap,40, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    block = drawRect(150,4.5*board.gap,110, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)
    block = drawRect(290,4.5*board.gap,350, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)


    block = drawRect(10,5.5*board.gap,170, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    block = drawRect(220,5.5*board.gap,150, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    block = drawRect(10+400,5.5*board.gap,50, board.border_width,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

    #princess blocks
    block = drawRect(100,board.border_width,board.border_width,50,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)
    block = drawRect(340,board.border_width,board.border_width,50,board.brown)
    board.allSprites.add(block)
    board.allBlocks.add(block)

class Stairs(object):

    stair = drawStair(370, 5.5*board.gap-5, board.ladder, 40, board.gap+10)
    board.allStairs.add(stair)
    board.allSprites.add(stair)
    c=-1
    for i in [300,360,240,450,255]:
        #print i
        stair = drawStair(i,(1.5+c)*board.gap-5, board.ladder ,40 ,board.gap+10)
        board.allStairs.add(stair)
        board.allbStairs.add(stair)
        c+=1

class BrokenStairs(object):
    #create broken stairs
    c=0
    for i in [(400,2.5*board.gap),(400,2.5*board.gap+80),(180,5.5*board.gap),(180,5.5*board.gap+80)]:
        bstair = drawStair(i[0],i[1]-5,board.ladder, 40, 2*board.border_width+5)
        board.allbStairs.add(bstair)
        if c%2!=0:
            board.allBlocks.add(bstair)
        board.allbBlocks.add(bstair)
        c+=1
