number = input('Введите любое вещественное число: ')
summa = 0
for i in number :
    if i.isdigit() :
        summa += int(i)
if number != 0 and summa == 0 :
    print("Вы ввели некорректное число. Повторите попытку")
else :
    print(f"Сумма цифр введённого числа равна {summa}")