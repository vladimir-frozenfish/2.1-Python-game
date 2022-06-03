import pygame

pygame.init()
pygame.display.set_caption('Text and Mouse status')

width = 1200
height = 700
win = pygame.display.set_mode((width, height))

"""работа с текстом"""
font = pygame.font.Font('fonts/GangSmallYuxian.ttf', 20)
text = font.render("Game over!", True, [255, 255, 255])
textpos = [10, 10]
x = 100

"""кнопки и окна для проверки состояни мыши"""
m_value = 0
m_button = ['-1', '+1', m_value]
m_size = [100, 50]
m_position = [(20, 100), (130, 100), (240, 100)]


life_game = True

while life_game:  # цикл пока life_game == true

    for event in pygame.event.get():  # цикл отслеживания действий игрока
        if event.type == pygame.QUIT:  # если игрок нажмет на закрытие, программа закроется
            life_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("Отжата кнопка: ", event.button)

    win.fill((0, 0, 0))  # заполнение экрана черным цветом

    """отображение изменяемого текста"""
    text1 = font.render(str(x), True, [255, 255, 255])
    win.blit(text1, (20, height-100))
    x -= 1

    mouse_position = pygame.mouse.get_pos()
    mouse_button = pygame.mouse.get_pressed()

    mouse_status_info = (f'mouse status: x = {mouse_position[0]} : '
                         f'y = {mouse_position[1]}, '
                         f'left button: {mouse_button[0]}, '
                         f'right button: {mouse_button[2]}, '
                         f'middle button: {mouse_button[1]}')
    text_mouse = font.render(mouse_status_info, True, [255, 255, 255])
    win.blit(text_mouse, (20, height - 50))

    """отображение кнопок и окна для проверки состояни мыши"""
    for i in range(len(m_button)):
        pygame.draw.rect(win, (255, 255, 255), (m_position[i][0], m_position[i][1], m_size[0], m_size[1]), width=1)
        m_text = font.render(str(m_button[i]), True, [255, 255, 255])
        win.blit(m_text, (m_position[i][0] + 40, m_position[i][1] + 15))

    if mouse_button[0]:
        if m_position[0][0] < mouse_position[0] < m_position[0][0]+m_size[0] and m_position[0][1] < mouse_position[1] < m_position[0][1]+m_size[1]:
            m_value -= 1
            m_button[2] = m_value

        if m_position[1][0] < mouse_position[0] < m_position[1][0]+m_size[0] and m_position[1][1] < mouse_position[1] < m_position[1][1]+m_size[1]:
            m_value += 1
            m_button[2] = m_value

    # задержка в мс
    pygame.time.delay(100)

    pygame.display.update()


pygame.quit()
