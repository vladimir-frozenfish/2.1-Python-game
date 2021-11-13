import pygame
import math
import random

pygame.init()
pygame.display.set_caption('Collision of balls')

width = 1200
height = 900
win = pygame.display.set_mode((width, height))
# win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# количество шаров
balls_value = 9

rB = []  # радиус шара
mB = []  # масса шара
xB = []  # координата X центра шара
yB = []  # координата Y центра шара
aB = []  # направление движения шара (от оси X по часовой стрелке)
vB = []  # скорость движения шара
cB = [0]  # цвет шара

for i in range(balls_value + 1):
    rB.append(round(8 * i + 6))
    mB.append(i ** 2)
    xB.append(round(i * i * 13))
    yB.append(int(height // 2))
    aB.append(random.random() * 2 * math.pi)
    vB.append((10 - i) / 2)
    cB.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

life_game = True

while life_game:  # цикл пока life_game == true

    for event in pygame.event.get():  # цикл отслеживания действий игрока
        if event.type == pygame.QUIT:  # если игрок нажмет на закрытие, программа закроется
            life_game = False

    win.fill((0, 0, 0))  # заполнение экрана черным цветом


    # прорисовка шаров
    for i in range(1, balls_value + 1):
        xB[i] += vB[i] * math.cos(aB[i])
        yB[i] += vB[i] * math.sin(aB[i])
        pygame.draw.circle(win, cB[i], (xB[i], yB[i]), rB[i])

    # задержка 10 мс
    pygame.time.delay(10)

    pygame.display.update()

    """Проверка на столкновение шара со стенами"""
    for i in range(1, balls_value + 1):
        if xB[i] <= rB[i] and (aB[i] > math.pi / 2 or aB[i] < -math.pi / 2):  # с левой стенкой
            aB[i] = math.pi - aB[i]
        if xB[i] >= width - rB[i] and (aB[i] > -math.pi / 2 and aB[i] < math.pi / 2):  # с правой стенкой
            aB[i] = math.pi - aB[i]
        if yB[i] <= rB[i] and (aB[i] < 0 and aB[i] > -math.pi):  # с верхней стенкой
            aB[i] = -aB[i]
        if yB[i] >= height - rB[i] and (aB[i] > 0 and aB[i] < math.pi):  # с нижней стенкой
            aB[i] = -aB[i]
        while aB[i] > math.pi: aB[i] -= 2 * math.pi
        while aB[i] < -math.pi: aB[i] += 2 * math.pi

    """Проверка на столкновение шара с другими шарами"""
    for i in range(1, balls_value + 1):
        for j in range(i + 1, balls_value + 1):
            # расстояние между шарами
            distance = ((xB[i] - xB[j]) ** 2 + (yB[i] - yB[j]) ** 2) ** 0.5
            if distance <= rB[i] + rB[j]:  # проверка на приближение шаров
                xB1new = xB[i] + vB[i] * math.cos(aB[i])
                yB1new = yB[i] + vB[i] * math.sin(aB[i])
                xB2new = xB[j] + vB[j] * math.cos(aB[j])
                yB2new = yB[j] + vB[j] * math.sin(aB[j])
                # ново расстояние между шарами, если бы движение продолжалось
                distance_new = ((xB1new - xB2new) ** 2 + (yB1new - yB2new) ** 2) ** 0.5
                if distance > distance_new:  # шары столкнулись при сближении
                    """Угол поворота луча (W) от центра шара (i) на центр шара (j),
                    с которым произошло столкновение"""
                    BB = math.atan((yB[j] - yB[i]) / (xB[j] - xB[i]))
                    if (xB[j] - xB[i] < 0):
                        BB += math.pi
                        while BB > math.pi / 2: BB -= 2 * math.pi
                        while BB < -math.pi / 2: BB += 2 * math.pi
                    """Угол от луча W (между центрами шаров) до направления движения шара"""
                    W1 = aB[i] - BB
                    W2 = aB[j] - BB

                    """Проекция скорости шара на луч W и на перпендикуляр
                    к нему (Wt) до столкновения"""
                    Vw1 = vB[i] * math.cos(W1)
                    Vw2 = vB[j] * math.cos(W2)
                    Vwt1 = vB[i] * math.sin(W1)
                    Vwt2 = vB[j] * math.sin(W2)

                    """Проекция скорости шара на луч W после столкновения
                    (проекция скорости на перпендикуляр к оси W не изменяется)"""
                    Vw1 = (2 * mB[j] * vB[j] * math.cos(W2) + (mB[i] - mB[j]) * vB[i] * math.cos(W1)) / (mB[i] + mB[j])
                    Vw2 = (2 * mB[i] * vB[i] * math.cos(W1) + (mB[j] - mB[i]) * vB[j] * math.cos(W2)) / (mB[i] + mB[j])

                    """Скорость шаров после столкновения"""
                    vB[i] = (Vw1 ** 2 + Vwt1 ** 2) ** 0.5
                    vB[j] = (Vw2 ** 2 + Vwt2 ** 2) ** 0.5

                    """Угол от луча W до направления движения после столкновения"""
                    W1 = math.atan(Vwt1/Vw1)
                    if Vw1 < 0: W1 += math.pi
                    W2 = math.atan(Vwt2/Vw2)
                    if Vw2 < 0: W2 += math.pi

                    """Новое результирующее направление движения после столкновения"""
                    aB[i] = BB + W1
                    while aB[i] > math.pi: aB[i] -= 2 * math.pi
                    while aB[i] < -math.pi: aB[i] += 2 * math.pi
                    aB[j] = BB + W2
                    while aB[j] > math.pi: aB[j] -= 2 * math.pi
                    while aB[j] < -math.pi: aB[j] += 2 * math.pi









pygame.quit()


