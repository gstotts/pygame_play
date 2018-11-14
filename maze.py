#!/usr/bin/env python

import pygame
from core import colors

COURSE = [[1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
          [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
          [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
          [1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 1, 1]]


class Maze:
    def __init__(self, width=300, height=300, fps=30):
        pygame.init()
        pygame.display.set_caption("Simple Maze v 1.0")
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.running = True
        self.time_played = 0.0
        self.x = int(self.width / 20)
        self.y = int(self.height / 20)
        self.box_row = 0
        self.box_column = 0

    def draw_course(self):
        self.screen.fill(colors.WHITE)
        line_height = self.height / len(COURSE)
        line_width = self.width / len(COURSE[0])
        cell_x, cell_y = (0, 0)

        for line in COURSE:
            for cell in line:
                if cell == 0:
                    pygame.draw.rect(self.screen, colors.BLACK, (cell_x, cell_y, line_width, line_height))
                cell_x = cell_x + line_width

            cell_x = 0
            cell_y = cell_y + line_height

        pygame.display.update()

    def draw_you(self):
        pygame.draw.circle(self.screen, colors.RED, (self.x, self.y), 10)
        pygame.display.update()

    def update_you(self):
        self.draw_course()
        pygame.draw.circle(self.screen, colors.RED, (self.x, self.y), 10)
        pygame.display.update()

    def run(self):
        self.draw_course()
        self.draw_you()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                        elif event.key == pygame.K_RIGHT and self.x != int(self.width / 20) * len(COURSE[0]) and \
                                COURSE[self.box_row][self.box_column + 1] != 0:
                            self.x += int(self.width / len(COURSE[0]))
                            if self.box_column != len(COURSE):
                                self.box_column += 1
                            self.update_you()
                        elif event.key == pygame.K_LEFT and self.x != int(self.height / 20) and \
                                COURSE[self.box_row][self.box_column - 1] != 0:
                            self.x -= int(self.width / len(COURSE[0]))
                            if self.box_column != 0:
                                self.box_column -= 1
                            self.update_you()
                        elif event.key == pygame.K_UP and self.y != int(self.height / 20) and \
                                COURSE[self.box_row - 1][self.box_column] != 0:
                            self.y -= int(self.height / len(COURSE[0]))
                            if self.box_row != 0:
                                self.box_row -= 1
                            self.update_you()
                        elif event.key == pygame.K_DOWN and self.y != int(self.height / 20) * len(COURSE[0]) and \
                                COURSE[self.box_row + 1][self.box_column] != 0:
                            self.y += int(self.height / len(COURSE[0]))
                            if self.box_row != len(COURSE[0]):
                                self.box_row += 1
                            self.update_you()
                    except IndexError:
                        pass

        pygame.quit()


if __name__ == '__main__':
    Maze(300, 300).run()
