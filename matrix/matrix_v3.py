import pygame as pg
import string
from random import choice, randrange


class Symbol:
    """класс символа"""
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)

    def draw(self, color):
        """отрисовка символа"""

        # изменение символа
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else lightgreen_katakana)

        # движение вниз символа
        '''
        if self.y < HEIGHT:
            self.y += self.speed
        else:
            self.y = -FONT_SIZE
        '''
        # можно одой строкой
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE

        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    """класс потока символов"""
    def __init__(self, x, y):
        self.column_height = randrange(8, 18)
        self.speed = randrange(1, 5)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        # [symbol.draw() for symbol in self.symbols]
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]


RES = WIDTH, HEIGHT = 1100, 900
FONT_SIZE = 30
alpha_value = 0

pg.init()

# monitor_size = RES = WIDTH, HEIGHT = pg.display.Info().current_w, pg.display.Info().current_h     # для полного экрана

screen = pg.display.set_mode(RES)
# screen = pg.display.set_mode(RES, pg.FULLSCREEN)                                                  # для полного экрана
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font('./../fonts/MS Mincho.ttf', FONT_SIZE, bold=True)
green_katakana = [font.render(char, True, (0, randrange(160, 256), 40)) for char in katakana]
lightgreen_katakana = [font.render(char, True, (144, 238, 144)) for char in katakana]
# green_katakana = [font.render(char, True, pg.Color('green')) for char in string.ascii_letters] # символы букв

# создание класса одного символа
# symbol = Symbol(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2, speed=4)

# создание класса потока символов
# symbol_column = SymbolColumn(WIDTH // 2 - FONT_SIZE // 2, HEIGHT // 2 - FONT_SIZE // 2)

# создание классов потоков символов для всего экрана
symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    # symbol.draw()
    # symbol_column.draw()
    [symbol_column.draw() for symbol_column in symbol_columns]

    if not pg.time.get_ticks() % 20 and alpha_value < 80:
        alpha_value += 3
        surface.set_alpha(alpha_value)

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)