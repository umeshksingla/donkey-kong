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
        for j in range(20):

            x1 = board.border_width + 4*board.border_width
            x2 = board.screen_width-100
            y1 = board.gap-20+c
            y2 = board.gap + 20 + c

            if y2 >= board.screen_height - 3*board.border_width - 20:
                y2 = board.screen_height - 3*board.border_width - 20
            if y1 >= board.screen_height - 3*board.border_width - 20:
                y1 = board.screen_height - 3*board.border_width - 20

            coin = Coin("Coin",
                random.uniform( x1, x2),
                random.uniform( y1, y2),
                board.coin,
                20,
                20
                )

            i=i+1
            if i%3==0:
                c+=board.gap
            board.allCoins.add(coin)

            #print  board.gap + 20 + c, board.gap-20+c
