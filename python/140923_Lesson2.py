print("14.09.2023 - Долгов Андрей / Rynn Lee")
choice = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\nВыбор: '))
if choice < 1 or choice > 4:
  print("Неверная операция!")
  exit()

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if choice == 1:
  print("Ответ сложение: ", a + b)
elif choice == 2:
  print("Ответ вычитание: ", a - b)
elif choice == 3:
  print("Ответ умножение: ", a * b)
else:
  if a == 0 or b == 0:
    print("Деление на ноль невозможно")
    exit()
  else:
    print("Ответ деление:\n a/b =", a/b, "\n b/a = ", b/a)