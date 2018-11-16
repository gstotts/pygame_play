#!/usr/bin/env python3

import random, pygame, sys
from core import colors

FPS = 30
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BOXSIZE = 40
GAPSIZE = 10
BOARD_WIDTH = 10
BOARD_HEIGHT = 7
X_MARGIN = int((WINDOW_WIDTH - (BOARD_WIDTH * (BOXSIZE + GAPSIZE))) / 2)
Y_MARGIN = int((WINDOW_HEIGHT - (BOARD_HEIGHT * (BOXSIZE + GAPSIZE))) / 2)

BGCOLOR = colors.NAVY
LIGHT_BGCOLOR = colors.GRAY
HIGHLIGHT = colors.BLUE

# Shapes
SQUARE = 0
DIAMOND = 1
OVAL = 2
TRIANGLE = 3

ALL_SHAPES = [SQUARE, DIAMOND, OVAL, TRIANGLE]

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
        print(board)

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