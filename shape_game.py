#!/usr/bin/env python3

import random, pygame, sys
from core import colors

FPS = 30
WINDOW_WIDTH = 510
WINDOW_HEIGHT = 510
BOXSIZE = 40
GAPSIZE = 10
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

BGCOLOR = colors.GRAY

# Shapes
SQUARE = 0
DIAMOND = 1
CIRCLE = 2
TRIANGLE = 3

ALL_SHAPES = [SQUARE, DIAMOND, CIRCLE, TRIANGLE]


class ShapeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Shape Game v1.0', '')
        self.running = True
        self.fps = FPS
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.bg = pygame.Surface(self.screen.get_size()).convert()

    def set_random_board(self):
        board = []
        for x in range(BOARD_HEIGHT):
            column = []
            for y in range(BOARD_WIDTH):
                column.append(random.choice(ALL_SHAPES))
            board.append(column)
        return board

    def draw_board(self, board):
        y = GAPSIZE
        self.screen.fill(BGCOLOR)
        for row in board:
            x = GAPSIZE
            for item in row:
                print (x, y, x + BOXSIZE, y + BOXSIZE)
                if item == SQUARE:
                    pygame.draw.rect(self.screen, colors.GREEN, (x, y, BOXSIZE, BOXSIZE))
                elif item == DIAMOND:
                    pygame.draw.polygon(self.screen, colors.BLUE, ((x + int(BOXSIZE * .5), y), \
                                                                   (x + BOXSIZE, y + int(BOXSIZE * .5)), \
                                                                   (x + int(BOXSIZE * .5), y + BOXSIZE), \
                                                                   (x, y + int(BOXSIZE * .5))))
                elif item == CIRCLE:
                    pygame.draw.circle(self.screen, colors.RED, (x + int(BOXSIZE / 2), \
                                                                 y + int(BOXSIZE / 2)), int(BOXSIZE / 2))
                else:
                    pygame.draw.polygon(self.screen, colors.YELLOW, ((x + int(BOXSIZE * .5), y), \
                                                                     (x + BOXSIZE, y + BOXSIZE), \
                                                                     (x, y + BOXSIZE)))
                x += (BOXSIZE + GAPSIZE)
            y += (BOXSIZE + GAPSIZE)

        pygame.display.update()

    def run(self):
        x, y = (0, 0)
        board = self.set_random_board()
        self.draw_board(board)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()


if __name__ == '__main__':
    ShapeGame().run()
