import pygame as pg


RES = WIDTH, HEIGHT = 1000, 200

pg.init()

pg.display.set_caption('Разрешение экрана')
monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]

screen = pg.display.set_mode(RES, pg.RESIZABLE)
surface = pg.Surface(RES)
clock = pg.time.Clock()

fullscreen = False

FONT_SIZE = HEIGHT // 100 * 8
font = pg.font.SysFont('arial.ttf', FONT_SIZE, bold=True)
text_resolution = f'Разрешение экрана: {WIDTH}, {HEIGHT}'


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        # отслеживание события нажатия клавиши
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F1:
                pass
            elif event.key == pg.K_F2:
                pass
            elif event.key == pg.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pg.display.set_mode((monitor_size), pg.FULLSCREEN)
                    RES_OLD = RES
                    RES = WIDTH, HEIGHT = screen.get_size()
                    surface = pg.Surface(RES)

                    FONT_SIZE = HEIGHT // 100 * 8
                    font = pg.font.SysFont('arial.ttf', FONT_SIZE, bold=True)
                    text_resolution = f'Разрешение экрана: {WIDTH}, {HEIGHT}'
                else:
                    screen = pg.display.set_mode((RES_OLD), pg.RESIZABLE)
                    RES = WIDTH, HEIGHT = screen.get_size()
                    surface = pg.Surface(RES)

                    FONT_SIZE = HEIGHT // 100 * 8
                    font = pg.font.SysFont('arial.ttf', FONT_SIZE, bold=True)
                    text_resolution = f'Разрешение экрана: {WIDTH}, {HEIGHT}'


        if event.type == pg.VIDEORESIZE:
            if not fullscreen:
                RES = WIDTH, HEIGHT = screen.get_size()
                screen = pg.display.set_mode((RES), pg.RESIZABLE)
                surface = pg.Surface(RES)

                FONT_SIZE = HEIGHT // 100 * 8
                font = pg.font.SysFont('arial.ttf', FONT_SIZE, bold=True)
                text_resolution = f'Разрешение экрана: {WIDTH}, {HEIGHT}'


    screen.blit(surface, (0, 0))
    surface.fill((100, 50, 100))

    text = font.render(text_resolution, True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.centerx = WIDTH // 2
    textRect.centery = HEIGHT // 2

    surface.blit(text, textRect)

    pg.display.flip()
    clock.tick(60)