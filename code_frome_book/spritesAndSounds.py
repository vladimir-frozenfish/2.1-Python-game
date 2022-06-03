import pygame, sys, random

from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

# настройка окна
WINDOWWIDTH = 800
WINDOWHEIGHT = 400
windowSurfase = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Спрайты и звуки!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создание структуры данных игрока и еды
playerSize = (50, 50)
player = pygame.Rect(300, 100, playerSize[0], playerSize[1])
playerImages = pygame.image.load('img/player.png')
playerStretchedImage = pygame.transform.scale(playerImages, playerSize)

foodSize = (40, 40)
foodImage = pygame.image.load('img/bomb.png')
foodStretchedImage = pygame.transform.scale(foodImage, foodSize)

foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - foodSize[0]), random.randint(0, WINDOWHEIGHT - foodSize[1]), foodSize[0], foodSize[1]))

foodCounter = 0
NEWFOOD = 40


# создание переменных перемещения
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# настройка музыки
pickUpSound = pygame.mixer.Sound('sound/8bit_bomb_explosion.wav')
pygame.mixer.music.load('sound/Cyberpunk Moonlight Sonata.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], foodSize[0], foodSize[1]))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - foodSize[0]), random.randint(0, WINDOWHEIGHT - foodSize[1]), foodSize[0], foodSize[1]))

    windowSurfase.fill(WHITE)

    # перемещение игрока
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.left += MOVESPEED

    # отображение игрока
    windowSurfase.blit(playerStretchedImage, player)

    # проверка, не пересекся ли игрок с какими-либо блоками еды
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImages, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()

    # отображение еды
    for food in foods:
        windowSurfase.blit(foodStretchedImage, food)

    pygame.display.update()
    mainClock.tick(60)







