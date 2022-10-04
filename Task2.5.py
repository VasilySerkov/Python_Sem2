N = int(input("Введите количество чисел в массиве: "))
Massive = [0] * N
from random import randint
for i in range(N):
    Massive[i] = randint(1, 100)
print("Исходный массив:", Massive)
for i in range(len(Massive)):
    j = randint(0, len(Massive) - 1)
    Temp = Massive[i]
    Massive[i] = Massive[j]
    Massive[j] = Temp
print("Перемешанный массив:", Massive)