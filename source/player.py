import sys
import pygame
import random
import os
from general_funcs import *
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_groups=[]):
        super().__init__(*sprite_groups)
        self.image = textures_container.get('player_img')
        self.rect = self.image.get_rect()
        # self.rect.x = 100
        # self.rect.y = 100

    def update(self):
        # self.rect.x += 1
        # self.rect.y += math.sin(self.rect.x) * 10
        # if self.rect.left > WIGTH:
        #     self.rect.right = 0
        pass
