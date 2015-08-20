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
    game_over = False

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
    change = 3
    up , down, left, right = (0,-1*change),(0, change),(-1*change,0),(change,0)
    upi , downi, lefti, righti = (0,0),(0,0),(change,0),(-1*change,0)
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

    #start and game over screen text display coordinates for reference
    startFontx = (screen_width - 2*border_width)/2-100
    startFonty = (screen_height - 2*border_width)/2 - 100

    #sprites
    allBorders = pygame.sprite.Group()
    allStairs = pygame.sprite.Group()
    allbStairs = pygame.sprite.Group()
    allBlocks = pygame.sprite.Group()
    allbBlocks = pygame.sprite.Group()
    allCoins = pygame.sprite.Group()
    allFireballs = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()  #except player
    princessSprite = pygame.sprite.Group()


class Rect(pygame.sprite.Sprite):

    def __init__(self,posx,posy,width,height,color):

        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

class Stair(pygame.sprite.Sprite):

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
    def __init__(self):
        #creating borders and storing its instance in borders
        for i in [(0,0),(0,board.screen_height-3*board.border_width)]:
            border = Rect(i[0], i[1], board.screen_width, board.border_width, board.dark_brown) #top
            board.allSprites.add(border)
            board.allBlocks.add(border)
            board.allbBlocks.add(border)
            board.allBorders.add(border)

        for i in [(0,0),(board.screen_width - board.border_width,0)]:
            border = Rect(i[0], i[1], board.border_width, board.screen_height, board.dark_brown) #top
            board.allSprites.add(border)
            board.allBlocks.add(border)
            board.allbBlocks.add(border)
            board.allBorders.add(border)

class Platforms(object):

    #creating blocks
    def __init__(self):

        coors = [
            (100, 50, 200),
            (10, 150, 350),
            (400, 150, 40),
            (180, 250, 60),
            (280, 250, 120),
            (440, 250, 190),
            (10, 350, 440),
            (490, 350, 40),
            (150, 450, 105),
            (290, 450, 345),
            (10, 550, 170),
            (220, 550, 150),
            (410, 550, 50)
        ]   # x-coor, y-coor, width
        for i in coors:
            block = Rect( i[0], i[1], i[2], board.border_width, board.brown)
            board.allSprites.add(block)
            board.allBlocks.add(block)
            board.allbBlocks.add(block)

        #princess side-blocks
        block = Rect(100,board.border_width,board.border_width,50,board.brown)
        board.allSprites.add(block)
        board.allBlocks.add(block)
        board.allbBlocks.add(block)

        block = Rect(340,board.border_width,board.border_width,50,board.brown)
        board.allSprites.add(block)
        board.allBlocks.add(block)
        board.allbBlocks.add(block)


class Stairs(object):

    def __init__(self):
        c=-1
        for i in [300,360,240,450,255,370]:
            #print i
            stair = Stair(i,(1.5+c)*board.gap-5, board.ladder ,40,board.gap+10)
            board.allStairs.add(stair)
            board.allbStairs.add(stair)
            c+=1

class BrokenStairs(object):
    #create broken stairs
    def __init__(self):
        c=0
        for i in [(400,2.5*board.gap),(400,2.5*board.gap+80),(180,5.5*board.gap),(180,5.5*board.gap+80)]:
            bstair = Stair(i[0],i[1]-5,board.ladder, 40, 2*board.border_width+5)
            board.allbStairs.add(bstair)
            if c%2==0:
                board.allBlocks.add(bstair)         # top part of broken ladder
            else:
                board.allStairs.add(bstair)         # bottom part of broken ladder
            c+=1
