#!/usr/bin/env python3


import pygame


class App(object):
    def __init__(self, width=640, height=400, fps=30):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        self.running = True
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.bg = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            ms = self.clock.tick(self.fps)
            self.playtime += ms / 1000.0
            self.draw_text(
                "FPS:  {:6.3}{}PLAYTIME:  {:6.3} SECONDS".format(self.clock.get_fps(), " " * 5, self.playtime))
            pygame.display.flip()
            self.screen.blit(self.bg, (0, 0))

        pygame.quit()

    def draw_text(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))


if __name__ == '__main__':
    App(640, 400).run()
