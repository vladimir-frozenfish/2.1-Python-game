import pygame, random, sys
from pygame.locals import *

# SETTINGS
WINDOWWIDTH = 800
WINDOWHEIGHT = 400
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60
BADDIEMINSIZE = 10
BADDIMAXSIZE = 40
ADDNEWBADDIRATE = 6
PLAYERMOVERATE = 5


def terminate ():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.collderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# настройка pygame, окна и указателя мыши
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ловкач!')
pygame.mouse.set_visible(False)

# настройка шрифтов
font = pygame.font.SysFont(None, 35)

# настройка звуков
gameOverSound = pygame.mixer.Sound('sound/GAMEOVER.wav')
pygame.mixer.music.load('sound/Cyberpunk Moonlight Sonata.mp3')

# настройка изображений
playerImage = pygame.image.load('img/player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('img/bomb.png')

# вывод начального экрана
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Ловкач', font, windowSurface, (WINDOWWIDTH // 3), (WINDOWHEIGHT // 3))
drawText('Нажмите любую клавишу для начала игры!', font, windowSurface, (WINDOWWIDTH // 5) - 30, (WINDOWHEIGHT // 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topscore = 0
while True:
    # настройка начала игры
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)


