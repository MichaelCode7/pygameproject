import sys
import pygame
import random
import os
from player import Player
from general_funcs import *


pygame.init()

# general vars
all_sprites = pygame.sprite.Group()


def main():
    # preload
    main_icon = textures_container.get('app_icon')
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Исследование подземелий')
    pygame.display.set_icon(main_icon)
    screen = pygame.display.set_mode(SIZE)
    running = True
    clock = pygame.time.Clock()

    # main load
    player = Player([all_sprites])

    # main loop
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
