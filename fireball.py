import pygame, layout
from pygame.locals import *


class Fireball(pygame.sprite.Sprite):

    def __init__(self, name, startx, starty, image, image_width, image_height):
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

        #self.position = layout.myFont.render(str("P Position : " + str(self.posx)+" , "+str(self.posy)), 1, blue)

    def update(self):
        pass
