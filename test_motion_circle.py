import pygame
import math

pygame.init() # запускает pygame

win = pygame.display.set_mode((1000, 1000))  # определение размера окна
pygame.display.set_caption("Моя первая игра") # аименование игры в окне
pygame.display.set_icon(pygame.image.load("images\ikonka.png")) # вставка иконки в окне


clock = pygame.time.Clock() #для работы с заданной частотой кадров

life_game = True # логическая переменная для жизни всего приложения

FPS = 60 # для обновления скорости экрана

position_earth_x = 1000 / 2
position_earth_y = 1000 / 2
radius_earth = 100

position_moon_x = position_earth_x + radius_earth + 100
position_moon_y = position_earth_y + radius_earth + 100
radius_moon = 50
radian_moon = 0

position_moon2_x = position_moon_x+radius_moon+20
position_moon2_y = position_moon_y+radius_moon+20
radius_moon2 = 20
radian_moon2 = 0

position_uran_x = position_earth_x + radius_earth + 250
position_uran_y = position_earth_y + radius_earth + 250
radius_uran = 30
radian_uran = 1


while life_game:  # цикл пока life_game == true
    # pygame.time.delay(100) # задержка в миллисекундах
    clock.tick(FPS)  # Держим цикл на правильной скорости
    win.fill((0, 0, 0))  # заполнение экрана черным цветом

    for event in pygame.event.get():  # цикл отслеживания действий игрока
        if event.type == pygame.QUIT:  # если игрок нажмет на закрытие, программа закроется
            life_game = False

    # земля
    pygame.draw.circle(win, (50,50,190), (position_earth_x, position_earth_y), radius_earth)
    pygame.draw.circle(win, (0, 0, 0), (position_earth_x, position_earth_y), 5)  # точка в центре круга

    # луна
    pygame.draw.circle(win, (50, 190, 50), (position_moon_x, position_moon_y), radius_moon)
    position_moon_x = (radius_earth+100+radius_moon) * math.cos(radian_moon*math.pi) + position_earth_x
    position_moon_y = -(radius_earth+100+radius_moon) * math.sin(radian_moon*math.pi) + position_earth_y
    radian_moon += 0.001

    # луна2
    pygame.draw.circle(win, (150, 150, 150), (position_moon2_x, position_moon2_y), 5)
    position_moon2_x = (radius_moon+20+radius_moon2) * math.cos(radian_moon2 * math.pi) + position_moon_x
    position_moon2_y = (radius_moon+20+radius_moon2) * math.sin(radian_moon2 * math.pi) + position_moon_y
    radian_moon2 += 0.005

    # уран
    pygame.draw.circle(win, (190, 50, 50), (position_uran_x, position_uran_y), radius_uran)
    position_uran_x = (radius_earth + 250 + radius_uran) * math.cos(radian_uran * math.pi) + position_earth_x
    position_uran_y = (radius_earth + 250 + radius_uran) * math.sin(radian_uran * math.pi) + position_earth_y
    radian_uran += 0.005

    pygame.display.flip()  # обновление экрана

pygame.quit()
