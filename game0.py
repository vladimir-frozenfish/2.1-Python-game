import pygame

pygame.init()   # запускает pygame

win = pygame.display.set_mode((750,750))    # определение размера окна
pygame.display.set_caption("Моя первая игра")   # наименование игры в окне
pygame.display.set_icon(pygame.image.load("images\ikonka.png"))     # вставка иконки в окне


clock = pygame.time.Clock()  #для работы с заданной частотой кадров

life_game = True    # логическая переменная для жизни всего приложения

FPS = 60 # для обновления скорости экрана

position_x = 20
position_y = 20
visota = 100
shirina = 100
speed = 5

is_prigok = False   # переменные для прыжка
prigok_count = 10


while life_game: # цикл пока life_game == true
    # pygame.time.delay(100) # задержка в милисекундах
    clock.tick(FPS) # Держим цикл на правильной скорости

    for event in pygame.event.get(): #цикл отслеживания действий игрока
        if event.type == pygame.QUIT: #если игрок нажмет на закрытие, программа закроется
            life_game = False

    keys = pygame.key.get_pressed() #в keys помещается нажатие клавиш
    if keys[pygame.K_RIGHT] and position_x < 740-shirina:  #при нажатии курсора квадратик перемещается со скоростью speed
        position_x += speed
    if keys[pygame.K_LEFT] and position_x > 10:
        position_x -= speed

    if is_prigok == False: # проверяется, если игрок в состоянии прыжка, то он не может еще раз прыгнуть и передвигаться вверх и вниз
        if keys[pygame.K_UP] and position_y > 10:
            position_y -= speed
        if keys[pygame.K_DOWN] and position_y < 740-visota:
            position_y += speed
        if keys[pygame.K_SPACE]:
            is_prigok = True # игрок переводится в состоянии прыжка
    else:
        if prigok_count >= -10:
            position_y -= prigok_count * abs(prigok_count) / 3 # прыгает по параболе
            prigok_count -= 1
        else:
            is_prigok = False
            prigok_count = 10

    if keys[pygame.K_q]: #при нажатии q квадратик расширяется от своего центра
        visota += 2
        shirina += 2
        position_x -= 1
        position_y -= 1

    if keys[pygame.K_w]: #при нажатии w квадратик уменьшается от своего центра
        visota -= 2
        shirina -= 2
        position_x += 1
        position_y += 1


    win.fill((0,0,0)) #заполнение экрана черным цветом
    pygame.draw.rect(win, (0, 0, 255), (position_x, position_y, visota, shirina)) #отображение квадрата
    #pygame.display.update() #обновление экрана
    pygame.display.flip()  # обновление экрана

pygame.quit()
