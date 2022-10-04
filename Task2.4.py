N = int(input("Введите любое натуральное число: "))
Number_Range = list(range(-N, N+1))
mltpl = 1
path = 'file.txt'
data = open(path, 'r')
for place in data:
    mltpl *= Number_Range[int(place)]
data.close()
print(Number_Range)
print(f"Произведение указанных элементов равно {mltpl}")