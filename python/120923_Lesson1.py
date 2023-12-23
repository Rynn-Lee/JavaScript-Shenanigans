import math
x = 7
y = 4
z = 8
h = 2
r = 3
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sum = 0
sum1 = 0
celsium = 25
fahrenheit = 77
longnum = 123456
pal = 8008

print("Долгов Андрей П4Б / RynnLee - 12.09.2023")
print("Задание - 1 | Сумма, разность, умножение, деление, остаток")
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

print("Задание - 2 | Возвести число в степерь")
print(x**2)

print("Задание - 3 | Найти корень числа")
print(math.sqrt(x))

print("Задание - 4 | Среднее арифметическое")
print((x+y)/2)

print("Задание - 5 | Фаренгейт и Цельсий")
print("C -> F", celsium*(9/5)+32)
print("F -> C", (fahrenheit-32)*(5/9))

print("Задание - 6 | Площадь прямоугольника")
print("S = ", x*y)

print("Задание - 7 | Площадь треугольника")
p = (x+y+z)/2
print("S = ", math.sqrt(p*(p-x)*(p-y)*(p-z)))

print("Задание - 8 | Объем куба")
print(x**3)

print("Задание - 9 | Площадь круга")
print(math.pi * (r**2))

print("Задание - 10 | Заданный процент от числа")
print((x/y)*100)

print("Задание - 11 | Длина окружности")
print(2*math.pi*r)

print("Задание - 12 | Периметр прямоугольника")
print((x+y)*2)

print("Задание - 13 | Диаметр окружности по радиусу")
print(2*r)

print("Задание - 14 | Наибольший общий делитель")
print(math.gcd(x, y))

print("Задание - 15 | Факториал числа")
print(math.factorial(x))

print("Задание - 16 | Сумму первых n натуральных чисел")
for number in num:
  sum = sum + number
print(sum)

print("Задание - 17 | Простое число")
for i in range(2, x - 1):
  if x % i == 0:
    print("Число непростое")
    break
  elif i == x - 2:
    print("Число простое")

print("Задание - 18 | Сумма цифр числа")
listedLongNum = list(str(longnum))
result = 0
for num in listedLongNum:
  result = int(num) + result
print(result)

print("Задание - 19 | Количество цифр в числе")
print(len(list(str(longnum))))

print("Задание - 20 | Палиндром")
listedNum = list(str(pal))
result = bool(listedNum == listedNum[::-1])
if result:
  print("Число палиндром")
else:
  print("Число не палиндром")
