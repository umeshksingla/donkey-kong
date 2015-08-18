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

    #speed and accelerate constants
    up , down, left, right = (0,-2),(0,2),(-2,0),(2,0)
    upi , downi, lefti, righti = (0,2),(0,-2),(2,0),(-2,0)
    acc_val = 0.25

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

    #sprites
    allBorders = pygame.sprite.Group()
    allStairs = pygame.sprite.Group()
    allBrokenStairs = pygame.sprite.Group()
    allBlocks = pygame.sprite.Group()
    allCoins = pygame.sprite.Group()
    allFireballs = pygame.sprite.Group()
    allSides = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()

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

board = Board()
class Platforms(object):

    #creating borders and storing its instance in borders
    for i in [(0,0),(0,board.screen_height-3*board.border_width)]:
        border = drawRect(i[0], i[1], board.screen_width, board.border_width, board.blue) #top
        board.allSprites.add(border)
        board.allBlocks.add(border)
        #allBorders.add(border)

    for i in [(0,0),(board.screen_width - board.border_width,0)]:
        border = drawRect(i[0], i[1], board.border_width, board.screen_height, board.blue) #top
        board.allSprites.add(border)
        board.allBlocks.add(border)
        board.allBorders.add(border)

    #creating blocks
    block1= drawRect(100,board.gap-50,240, board.border_width,board.red)
    board.allSprites.add(block1)
    board.allBlocks.add(block1)
    block2 = drawRect(10,1.5*board.gap,400, board.border_width,board.red)
    board.allSprites.add(block2)
    board.allBlocks.add(block2)
    block3 = drawRect(180,2.5*board.gap,450, board.border_width,board.red)
    board.allSprites.add(block3)
    board.allBlocks.add(block3)
    block4 = drawRect(10,3.5*board.gap,480, board.border_width,board.red)
    board.allSprites.add(block4)
    board.allBlocks.add(block4)
    block5 = drawRect(150,4.5*board.gap,480, board.border_width,board.red)
    board.allSprites.add(block5)
    board.allBlocks.add(block5)
    block6 = drawRect(10,5.5*board.gap,360, board.border_width,board.red)
    board.allSprites.add(block6)
    board.allBlocks.add(block6)
    block6 = drawRect(10+400,5.5*board.gap,50, board.border_width,board.red)
    board.allSprites.add(block6)
    board.allBlocks.add(block6)

    #princess blocks
    block7 = drawRect(100,board.border_width,board.border_width,50,board.red)
    board.allSprites.add(block7)
    board.allBlocks.add(block7)
    block8 = drawRect(340,board.border_width,board.border_width,50,board.red)
    board.allSprites.add(block8)
    board.allBlocks.add(block8)

    c=-1
    for i in [300,360,240,450,255]:
        #print i
        stair = drawRect(i,(1.5+c)*board.gap, board.border_width,board.gap+10,board.green)
        board.allStairs.add(stair)
        board.allSprites.add(stair)
        c+=1

    #create broken stairs
    c=0
    for i in [(400,2.6*board.gap),(400,3.2*board.gap)]:
        bstair = drawRect(i[0],i[1], board.border_width, 2.5*board.border_width, board.green)
        board.allSprites.add(bstair)
        board.allBrokenStairs.add(bstair)
        c+=1
