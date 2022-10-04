n = input("Введите натуральное число: ")
while not n.isdigit() :
    n = input("Вы ввели некорректное число. Повторите ввод: ")
n = int(n)
result = list()
j = 1
for i in range (n):
    j *= (i + 1)
    result.append(j)
print(result)