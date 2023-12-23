print("Долгов Андрей П4Б / Rynn Lee")
import math

#-----------------Ex 1-------------------------
class Shape:
  def area(self):
    pass

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

class Circle(Shape):
  def __init__(self, radius):
      self.radius = radius

  def area(self):
      return math.pi * self.radius ** 2

rectangle = Rectangle(5, 3)
circle = Circle(4)

print("Площадь прямоугольника:", rectangle.area())
print("Площадь круга:", circle.area())

#-----------------Ex 2-------------------------
class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def start(self):
    print(f"Запуск автомобиля {self.make} {self.model}")

class ToyotaCar(Car):
  def start(self):
    print(f"Запуск автомобиля {self.make} {self.model} в режиме гибрида")

class BMWCar(Car):
  def start(self):
    print(f"Запуск автомобиля {self.make} {self.model} в спортивном режиме")

car1 = Car("Nissan", "Maxima")
car2 = ToyotaCar("Toyota", "Prius")
car3 = BMWCar("BMW", "X5")

car1.start()
car2.start()
car3.start()

#-----------------Ex 3-------------------------
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    print(f"{self.name} гавкает")

class Cat(Animal):
  def make_sound(self):
    print(f"{self.name} мяукает")

animal1 = Dog("Бобик", "Собака")
animal2 = Dog("Рекс", "Собака")
animal3 = Cat("Мурка", "Кошка")

animal1.make_sound()
animal2.make_sound()
animal3.make_sound()