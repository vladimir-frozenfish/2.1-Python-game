import random
import numpy

n = random.random()
print(n)

a = random.randint(1,100)  # случайное число от 1 до 100
print(a)

b = random.randrange(0,100,5)  # случайное число от 1 до 100 с шагом 5
print(b)

spisok = ["Apple","Ananas","Arbuz","Cherry","Dynya","Grape"]
s = random.choice(spisok)  # случайны выбор из списка
print(s)

s_1 = random.sample(spisok,3)  # случайный выбор нескольких элементов из списка, но неболье самого списка
print(s_1)

s_2 = random.choices(spisok, k=20) # случайный выбор заданного количества элементов из списка
print(s_2)

random.shuffle(spisok)  # перемешивания списка
print(spisok)

random_array1 = numpy.random.random_integers(1,100,10)
print(random_array1)

random_integer_array = numpy.random.random_integers(1, 10, size=(3, 2))
print("2-мерный массив случайных целых чисел \n", random_integer_array)

for i in range(10,-1,-1):
    print(i)