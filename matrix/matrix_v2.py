import pygame as pg
import random


class MatrixLetters:
    def __init__(self, app):
        self.app = app
        # self.letters = '1234567890ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        self.letters = [chr(int('0x30a0', 16) + i) for i in range(96)]
        self.font_size = 10
        # self.font = pg.font.SysFont('arial', self.font_size, bold=True)
        self.font = pg.font.Font('./../fonts/MS Mincho.ttf', self.font_size, bold=True)
        self.columns = app.WIDTH // self.font_size
        self.drops = [0 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, True, (0, 255, 0))
            pos = i * self.font_size, (self.drops[i]) * self.font_size
            self.app.surface.blit(char_render, pos)

            if self.drops[i] * self.font_size > self.app.HEIGHT and random.uniform(0, 1) > 0.975:
                self.drops[i] = -1
            self.drops[i] += 1

    def run(self):
        self.draw()


class MatrixApp:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1000, 700

        pg.init()

        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)

        self.clock = pg.time.Clock()

        self.matrixLetters = MatrixLetters(self)

    def draw(self):
        self.surface.fill((0, 0, 0, 10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(25)


if __name__ == '__main__':
    app = MatrixApp()
    app.run()
