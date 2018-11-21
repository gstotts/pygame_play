#!/usr/bin/env python3

import random, pygame, sys
from core import colors

FPS = 30
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
BOXSIZE = 20
GAPSIZE = 10
BOARD_WIDTH = int((WINDOW_WIDTH - GAPSIZE)/(BOXSIZE + GAPSIZE))
BOARD_HEIGHT = int((WINDOW_HEIGHT - GAPSIZE)/(BOXSIZE + GAPSIZE))

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

    def get_box_top_coords(self, box_x, box_y):
        x = box_x * (BOXSIZE + GAPSIZE)
        y = box_y * (BOXSIZE + GAPSIZE)

    def get_box_from_position(self, x, y):
        for box_x in range(BOARD_WIDTH):
            for box_y in range(BOARD_HEIGHT):
                box = pygame.Rect(box_x * (BOXSIZE + GAPSIZE) + GAPSIZE, box_y * (BOXSIZE + GAPSIZE) + GAPSIZE , BOXSIZE, BOXSIZE)
                if box.collidepoint(x, y):
                    return (box_x, box_y)
        return(None, None)

    def get_group_touching(self, position, shape, board):
        queue = [position]
        same_shape_and_touching = []
        while queue != []:
            (x, y) = queue.pop()
            same_shape_and_touching.append((x, y))
            if BOARD_WIDTH > x + 1:
                if (board[x + 1][y] == shape) and ((x + 1, y) not in same_shape_and_touching):
                    queue.append((x + 1, y))
            if x - 1 >= 0:
                if (board[x - 1][y] == shape) and ((x - 1, y) not in same_shape_and_touching):
                    queue.append((x - 1, y))
            if y - 1 >= 0:
                if (board[x][y - 1] == shape) and ((x, y - 1) not in same_shape_and_touching):
                    queue.append((x, y - 1))
            if BOARD_HEIGHT > y + 1:
                if (board[x][y + 1] == shape) and ((x, y + 1) not in same_shape_and_touching):
                    queue.append((x, y + 1))

        if len(same_shape_and_touching) > 1:
            return same_shape_and_touching
        else:
            return None







    def run(self):
        x, y = (0, 0)
        board = self.set_random_board()
        self.draw_board(board)
        print(board)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        (y, x) = event.pos
                        (box_x, box_y) = self.get_box_from_position(x, y)
                        if (box_x, box_y) != (None, None):
                            shape = board[box_x][box_y]
                            coords_to_remove = self.get_group_touching((box_x, box_y), shape, board)
                            if coords_to_remove == None:
                                pass
                            else:
                                print(coords_to_remove)


if __name__ == '__main__':
    ShapeGame().run()