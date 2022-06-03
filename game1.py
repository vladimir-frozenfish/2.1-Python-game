# прыгающий мячик
import pygame

pygame.init()  # запускает pygame

# объявление переменных
display_width = 1000
display_height = 750

earth_eight = 50
position_x = 100
radius_shar = 5
position_y = display_height-(earth_eight+radius_shar)
speed = 5

is_prigok = False # переменные для прыжка
prigok_count = 10
prigok_count_ryad = 2

clock = pygame.time.Clock() #для работы с заданной частотой кадров
life_game = True # логическая переменная для жизни всего приложения
FPS = 60 # для обновления скорости экрана

win = pygame.display.set_mode((display_width,display_height))  # определение размера окна
pygame.display.set_caption("Прыгающий шарик")  # наименование игры в окне
pygame.display.set_icon(pygame.image.load("images\ikonka.png")) # вставка иконки в окне


while life_game: # цикл пока life_game == true
    # pygame.time.delay(100) # задержка в милисекундах
    clock.tick(FPS) # Держим цикл на правильной скорости

    for event in pygame.event.get(): #цикл отслеживания действий игрока
        if event.type == pygame.QUIT: #если игрок нажмет на закрытие, программа закроется
            life_game = False

    keys = pygame.key.get_pressed() #в keys помещается нажатие клавиш
    if keys[pygame.K_RIGHT] and position_x < display_width-radius_shar:  #при нажатии курсора квадратик перемещается со скоростью speed
        position_x += speed
    if keys[pygame.K_LEFT] and position_x > radius_shar:
        position_x -= speed

    if is_prigok == False: # проверяется, если игрок в состоянии прыжка, то он не может еще раз прыгнуть и передвигаться вверх и вниз
        if keys[pygame.K_UP] and position_y > radius_shar:
            position_y -= speed
        if keys[pygame.K_DOWN] and position_y < display_height-radius_shar-earth_eight:
            position_y += speed
        if keys[pygame.K_SPACE]:
            is_prigok = True # игрок переводится в состоянии прыжка
    else:
        if prigok_count_ryad <= 6:
            if prigok_count >= -10:
                position_y -= prigok_count * abs(prigok_count) / prigok_count_ryad # прыгает по параболе
                prigok_count -= 1
            else:
                prigok_count = 10
                prigok_count_ryad += 1
        else:
            is_prigok = False
            prigok_count_ryad = 2

    if keys[pygame.K_q]: #при нажатии q квадратик расширяется от своего центра
        radius_shar += 1

    if keys[pygame.K_w]: #при нажатии w квадратик уменьшается от своего центра
        radius_shar -= 1


    win.fill((0,0,0)) #заполнение экрана черным цветом
    pygame.draw.circle(win, (100, 20, 200), (position_x, position_y), radius_shar) #  отображение круга
    pygame.draw.rect(win, (255, 0, 0), (0, display_height-earth_eight, display_width, earth_eight))  # отображение земли
    #pygame.display.update() #обновление экрана
    pygame.display.flip()  # обновление экрана

pygame.quit()
