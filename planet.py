import pygame
import random
import math

pygame.init()


# класс игрового поля, в качестве x,y передается размеры экрана
class IgrovoePole:
    def __init__(self, x, y):
        self.up = 20
        self.down = 70
        self.left = 20
        self.right = 20
        self.line = 1
        self.width = x - self.left - self.right
        self.height = y - self.up - self.down


# класс препятствие прямоугольник
class Barier:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.width = 500
        self.height = 50
        self.speed = 5

    def motion_right(self):
        self.x += self.speed

    def motion_left(self):
        self.x -= self.speed

    def motion_up(self):
        self.y -= self.speed

    def motion_down(self):
        self.y += self.speed


# класс планет
class Planet:
    def __init__(self, classIgrovoePole):  # ширина, высота и отступы слева и сверху игрового поля
        self.width = classIgrovoePole.width
        self.height = classIgrovoePole.height
        self.left = classIgrovoePole.left
        self.up = classIgrovoePole.up
        self.x = self.width / 2 + self.left  # начальные координаты круга посередине поля
        self.y = self.height / 2 + self.up
        self.radius = 50  # радиус круга
        self.speed = 4
        self.napravlenie_x = 1
        self.napravlenie_y = 1
        self.color = (25, 150, 50)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def motion(self):
        self.x += self.speed * self.napravlenie_x  # смещение круга по x
        self.y += self.speed * self.napravlenie_y  # смещение круга по y

    def motion_change(self):
        if self.x >= self.width + self.left - self.radius or self.x <= self.left + self.radius:
            self.napravlenie_x *= -1
        if self.y >= self.height + self.up - self.radius or self.y <= self.up + self.radius:
            self.napravlenie_y *= -1

    def motion_change_x(self):
        self.napravlenie_x *= -1

    def motion_change_y(self):
        self.napravlenie_y *= -1

    def random_size_position(self):
        self.radius = random.randint(5, 50)
        self.x = random.randint(self.left + self.radius, self.width - self.radius)
        self.y = random.randint(self.up + self.radius, self.height - self.radius)
        self.speed = random.randint(1, 5)
        self.napravlenie_x = random.choice([-1, 1])
        self.napravlenie_y = random.choice([-1, 1])
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


class Moon:
    def __init__(self, classPlanet):
        self.radius = 30
        self.distance = 100
        self.radius_motion = self.radius + self.distance + classPlanet.radius
        self.x = classPlanet.x
        self.y = classPlanet.y
        self.radian = 1
        self.speed = 0.01
        self.color = (25, 151, 200)
        self.direction = 1

    def motion_circle(self, classPlanet):
        self.x = (self.radius + self.distance + classPlanet.radius) * math.cos(self.radian * math.pi) + classPlanet.x
        self.y = self.direction * (self.radius + self.distance + classPlanet.radius) * math.sin(self.radian * math.pi) + classPlanet.y
        self.radian += self.speed
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


# функция проверки на столкновение с препятствием
def stolknovenie_barier(circle, barier):
    if circle.x >= barier.x + barier.width:
        if circle.x - circle.radius <= barier.x + barier.width \
                and barier.y + barier.height > circle.y > barier.y:  # and circle.napravlenie_x == -1:
            circle.motion_change_x()

    if circle.x <= barier.x:
        if circle.x + circle.radius >= barier.x \
                and barier.y + barier.height > circle.y > barier.y:  # and circle.napravlenie_x == -1:
            circle.motion_change_x()

    if circle.y <= barier.y:
        if circle.y + circle.radius >= barier.y \
                and barier.x + barier.width > circle.x > barier.x:  # and circle.napravlenie_x == -1:
            circle.motion_change_y()

    if circle.y >= barier.y + barier.height:
        if circle.y - circle.radius <= barier.y + barier.height \
                and barier.x + barier.width > circle.x > barier.x:  # and circle.napravlenie_x == -1:
            circle.motion_change_y()

# объявление переменных размер экрана
display_width = 1050
display_height = 800

clock = pygame.time.Clock()  # для работы с заданной частотой кадров
life_game = True  # логическая переменная для жизни всего приложения
FPS = 60  # для обновления скорости экрана

win = pygame.display.set_mode((display_width, display_height))  # определение размера окна
pygame.display.set_caption("Двигающиеся круги")  # наименование игры в окне
pygame.display.set_icon(pygame.image.load("images\ikonka.png"))  # вставка иконки в окне

# создание объекта игрового поля
igrovoe_pole = IgrovoePole(display_width, display_height)

# фон
background = pygame.image.load('images\stars-1010x810.jpg')

# создание объекта класса Planet
circle = Planet(igrovoe_pole)
circle.radius = 50
circle_images = pygame.image.load('images\planet_red-radius-50.png')

# создание второго объекта класса Planet
circle_1 = Planet(igrovoe_pole)
circle_1.napravlenie_y = -1
circle_1.speed = 1

# создание объекта класса Moon, в качестве параметра вносится объект класса Planet, вокруг которого будет вращаться данный объект
sputnik_2 = Moon(circle_1)
sputnik_2.speed = 0.001

sputnik_3 = Moon(circle_1)
sputnik_3.direction = -1
sputnik_3.distance = 30
sputnik_3.radius = 10
sputnik_3.speed = 0.001
sputnik_3.color = (255, 0, 0)

# создание спутника для спутника
sputnik_4 = Moon(sputnik_2)
sputnik_4.distance = 10
sputnik_4.radius = 10
sputnik_4.color = (255, 255, 255)
sputnik_4.direction = -1

# создание массива объектов класса Planet с рандомными характеристиками
planets_list = []
for i in range(10):
    planets_list.append(Planet(igrovoe_pole))
    planets_list[i].random_size_position()
i = 0

# создание объекта класса Barier - прямоугольное препятствие
barier_01 = Barier()
barier_01_images = pygame.image.load('images\_barier500x50.png')

while life_game:  # цикл пока life_game == true
    clock.tick(FPS)  # Держим цикл на правильной скорости

    for event in pygame.event.get():  # цикл отслеживания действий игрока
        if event.type == pygame.QUIT:  # если игрок нажмет на закрытие, программа закроется
            life_game = False

    keys = pygame.key.get_pressed()  # в keys помещается нажатие клавиш

    win.fill((0, 0, 0))  # заполнение экрана черным цветом

    # фон
    win.blit(background, (igrovoe_pole.left, igrovoe_pole.up))

    # отображение границы поля
    pygame.draw.rect(win, (250, 250, 250),
                     (igrovoe_pole.left, igrovoe_pole.up, igrovoe_pole.width, igrovoe_pole.height), igrovoe_pole.line)

    # отображение препятствия и отображения спрайта на препятствии такого же размера, движение барьера от нажатий клавиш
    pygame.draw.rect(win, (25, 150, 50), (barier_01.x, barier_01.y, barier_01.width, barier_01.height))
    win.blit(barier_01_images, (barier_01.x, barier_01.y))
    if keys[pygame.K_RIGHT]:
        barier_01.motion_right()
    if keys[pygame.K_LEFT]:
        barier_01.motion_left()
    if keys[pygame.K_UP]:
        barier_01.motion_up()
    if keys[pygame.K_DOWN]:
        barier_01.motion_down()


    # отображение круга в границах экрана
    circle.draw(win)
    win.blit(circle_images, (circle.x - circle.radius - 10, circle.y - circle.radius - 10))
    circle.motion()  # движение круга по x и y, изменение направления в границах игрового поля
    circle.motion_change()
    stolknovenie_barier(circle, barier_01)  # функция проверки столкновения круга с препятствием

    circle_1.draw(win)
    circle_1.motion()  # движение второго круга
    circle_1.motion_change()

    # рисование круга спутника как объекта класса в движение по орбите
    sputnik_2.motion_circle(circle_1)
    sputnik_3.motion_circle(circle_1)

    sputnik_4.motion_circle(sputnik_2)

    # рисование кругов из массива объектов planets_list
    for i in range(len(planets_list)):
        planets_list[i].draw(win)
        planets_list[i].motion()
        planets_list[i].motion_change()
        stolknovenie_barier(planets_list[i], barier_01)

    pygame.display.flip()  # обновление экрана

pygame.quit()
