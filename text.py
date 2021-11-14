import pygame

pygame.init()
pygame.display.set_caption('Collision of balls')

width = 1200
height = 700
win = pygame.display.set_mode((width, height))

"""работа с текстом"""
font = pygame.font.Font('font/GangSmallYuxian.ttf', 20)
text = font.render("Game over!", True, [255, 255, 255])
textpos = [10, 10]
x = 100


life_game = True

while life_game:  # цикл пока life_game == true

    for event in pygame.event.get():  # цикл отслеживания действий игрока
        if event.type == pygame.QUIT:  # если игрок нажмет на закрытие, программа закроется
            life_game = False

    win.fill((0, 0, 0))  # заполнение экрана черным цветом

    """отображение передвигаемого статичекого текста"""
    win.blit(text, textpos)
    textpos[0] += 1
    textpos[1] += 1

    """отображение изменяемого текста"""
    text1 = font.render(str(x), True, [255, 255, 255])
    win.blit(text1, (20, height-100))
    x -= 1
    if x == 0:
        life_game = False


    text_mouse = font.render('mouse status:', True, [255, 255, 255])
    win.blit(text_mouse, (20, height - 50))

    # задержка в мс
    pygame.time.delay(100)

    pygame.display.update()


pygame.quit()
