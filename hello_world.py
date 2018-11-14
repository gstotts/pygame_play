#!/usr/bin/env python

import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    display_surface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello World!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
