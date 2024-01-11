import sys
import pygame
import random
import os

# funcs


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# textures container and vars
# in the future I plan to implement the character from different angles using a sprite sheets
textures_container = {
    'app_icon': load_image('imgs/potion_main_icon.png'),
    'player_img': load_image('imgs/entitysheets/player.png')
}

SIZE = (1200, 800)
WIGTH, HEIGHT = SIZE
FPS = 35
