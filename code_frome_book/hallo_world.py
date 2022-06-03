import pygame
import sys

from pygame.locals import *

# настройка pygame
pygame.init()

# настройка окна
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hallo world!')

# назначение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# назначение шрифтов
basicFont = pygame.font.SysFont(None, 48)

# настройка текста
text = basicFont.render('Hallo World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# нанесение на поверхность белого фона
windowSurface.fill(WHITE)

# нанесение на поверхность зеленого многоугольника
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291, 106), (236,277), (56, 277), (0, 106)))

# нанесение на поверхность синих линий
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 8)

# нанесение на поверхность синего круга
pygame.draw.circle(windowSurface, BLUE, (30, 50), 20, 0)

# нанесение на поверхность красного эллипса
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# нанесение на поверхность фонового прямоугольника для текста
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# получение массива пикселов поверхности
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# нанесение текста на поверхность
windowSurface.blit(text, textRect)

# отображение окна на экране
pygame.display.update()

# запуск игрового цикла
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

