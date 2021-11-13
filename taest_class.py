import random

# класс дисплея, определяет разрешение дисплея
class Screen:
    def __init__(self):
        self.width = 1000
        self.height = 750
        self.x = random.randint(0,100)

class IgrovoePole:
    def __init__(self, x, y):
        self.up = 10
        self.down = 50
        self.left = 30
        self.right = 30
        self.line = 1
        self.width = x - self.left - self.right
        self.height = y - self.up - self.down

def foo(a,b):  # передача в функцию двух объектов
    print(a.width)
    a.width = 500
    print(a.width)

x = Screen()
print(x)
y = IgrovoePole(5,10)
foo(x,y)
print(x.width)

'''
display = Screen()
print(display)

pole = IgrovoePole(display.width, display.height)
print(pole.width, pole.height)

spisok_screen = [Screen(), Screen(), Screen()]

for i in range(len(spisok_screen)):
    print(i, spisok_screen[i].width, spisok_screen[i].height, spisok_screen[i].x)
'''