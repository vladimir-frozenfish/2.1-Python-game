import pygame, sys, time
from pygame.locals import *

pygame.init()

# настройка окна
WINDOWWIDTH = 800
WINDOWHEIGHT = 400
windowSurfase = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Анимация!')

# создание переменных направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создание структуры данных блока
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir': UPLEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWNLEFT}
boxes = [b1, b2, b3]

# запуск игрового цикла
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurfase.fill(WHITE)

    for b in boxes:
        # перемещение структуры данных блока
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        # проверка, переместился ли блок за пределы окна
        if b['rect'].top < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        pygame.draw.rect(windowSurfase, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(0.02)





