n = input("Введите натуральное число: ")
while not n.isdigit() :
    n = input("Вы ввели некорректное число. Повторите ввод: ")
n = int(n)
result = dict()
for i in range(1, n+1):
    result[i] = round((1 + 1 / i) ** i)
summa = 0
for i in result:
    summa += result[i]
print(f"Для {n} cумма последовательности чисел {result} равна {summa}")