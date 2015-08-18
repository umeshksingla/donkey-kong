######## Aug 16, 2015 ########
######## Umesh Singla ########

import pygame, layout, random
from pygame.locals import *

board = layout.Board()
class Coin(pygame.sprite.Sprite):

    def __init__(self, name, startx, starty, image, image_width, image_height):
        pygame.sprite.Sprite.__init__(self)

        self.name = name

        self.posx = startx
        self.posy = starty

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(image_width,image_height))

        self.rect = self.image.get_rect()
        self.rect.x = startx;
        self.rect.y = starty;

        #self.position = layout.myFont.render(str("P Position : " + str(self.posx)+" , "+str(self.posy)), 1, blue)

class drawCoins(object):

    def __init__(self):
        c=0
        i=0
        # generate coins
        for i in range(20):
            coin = Coin("Coin",
                random.uniform( board.border_width + 4*board.border_width, board.screen_width-100),
                random.uniform(  board.gap-20+c, board.gap + 20 + c),
                board.coin,
                20,
                20
                )
            i=i+1
            if i%3==0:
                c+=board.gap
            board.allCoins.add(coin)
            board.allSprites.add(coin)

            #print  board.gap + 20 + c, board.gap-20+c
