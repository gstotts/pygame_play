#!/usr/bin/env python3
import numpy
import pygame
import random

from core import colors

FPS = 30
SCORE_TRACKER_HEIGHT = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480 + SCORE_TRACKER_HEIGHT
BOXSIZE = 20
GAPSIZE = 10
BOARD_WIDTH = int((WINDOW_WIDTH - GAPSIZE) / (BOXSIZE + GAPSIZE))
BOARD_HEIGHT = int((WINDOW_HEIGHT - GAPSIZE - SCORE_TRACKER_HEIGHT) / (BOXSIZE + GAPSIZE))

BGCOLOR = colors.GRAY

# Shapes
SQUARE = 0
DIAMOND = 1
CIRCLE = 2
TRIANGLE = 3
EMPTY = 4

ALL_SHAPES = [SQUARE, DIAMOND, CIRCLE, TRIANGLE]


class ShapeGame:
    def __init__(self):
        """Initializes the game and sets basic settings."""
        pygame.init()
        pygame.display.set_caption('Shape Game v1.0', '')
        self.running = True
        self.fps = FPS
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

    @staticmethod
    def set_random_board():
        """Returns a randomly arranged board based on shapes listed in the ALL_SHAPES constant."""
        return numpy.random.randint(len(ALL_SHAPES), size=(BOARD_HEIGHT, BOARD_WIDTH))

    def draw_board(self, board):
        """Accepts a 2-d list and returns the graphical representation of the board."""
        y = GAPSIZE
        self.screen.fill(BGCOLOR)
        for row in board:
            x = GAPSIZE
            for item in row:
                if item == SQUARE:
                    pygame.draw.rect(self.screen, colors.GREEN, (x, y, BOXSIZE, BOXSIZE))
                elif item == DIAMOND:
                    pygame.draw.polygon(self.screen, colors.BLUE, ((x + int(BOXSIZE * .5), y),
                                                                   (x + BOXSIZE, y + int(BOXSIZE * .5)),
                                                                   (x + int(BOXSIZE * .5), y + BOXSIZE),
                                                                   (x, y + int(BOXSIZE * .5))))
                elif item == CIRCLE:
                    pygame.draw.circle(self.screen, colors.RED, (x + int(BOXSIZE / 2), y + int(BOXSIZE / 2)),
                                       int(BOXSIZE / 2))
                elif item == TRIANGLE:
                    pygame.draw.polygon(self.screen, colors.YELLOW, ((x + int(BOXSIZE * .5), y),
                                                                     (x + BOXSIZE, y + BOXSIZE), (x, y + BOXSIZE)))
                else:
                    pass  #Skip EMPTY spaces

                x += (BOXSIZE + GAPSIZE)
            y += (BOXSIZE + GAPSIZE)

        pygame.display.update()

    @staticmethod
    def get_box_from_position(x, y):
        """Accepts x and y coordinates of mouse click and returns the x and y position on the board."""
        for box_x in range(BOARD_WIDTH):
            for box_y in range(BOARD_HEIGHT):
                box = pygame.Rect(box_x * (BOXSIZE + GAPSIZE) + GAPSIZE, box_y * (BOXSIZE + GAPSIZE) + GAPSIZE, BOXSIZE,
                                  BOXSIZE)
                if box.collidepoint(x, y):
                    return box_x, box_y
        return None, None

    @staticmethod
    def get_group_touching(position, shape, board):
        """Accepts a position on the board as a list, a shape clicked, and the board in use and returns the positions
        of all shapes touching that series."""
        queue = [position]
        same_shape_and_touching = []
        while queue:
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

    def remove_shapes(self, shapes_to_remove, board):
        """Removes shapes that were touching after click, shift items down, and then redraws board."""
        # Replace shapes at (x,y) coordinates with emtpy spots
        for (x, y) in shapes_to_remove:
            board[x][y] = EMPTY

        # Shift shapes down if needed
        col_val = 0
        for column in numpy.transpose(board):

            if EMPTY in column:
                stripped_column = list(filter(lambda a: a != EMPTY, column))
                while len(stripped_column) != BOARD_HEIGHT:
                    stripped_column.insert(0, EMPTY)
                board[:, col_val] = stripped_column
            col_val += 1
        self.draw_board(board)


    def run(self):
        """Runs the basic while loop for game play and handles events."""
        board = self.set_random_board()
        self.draw_board(board)
        while self.running:
            for event in pygame.event.get():
                # If a user wants to quit, do so gracefully.
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
                            if coords_to_remove != None:
                                if len(coords_to_remove) >= 3:
                                    self.remove_shapes(coords_to_remove, board)


if __name__ == '__main__':
    ShapeGame().run()
