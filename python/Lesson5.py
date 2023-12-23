print("Долгов Андрей П4Б / Rynn Lee")

#Ex 1
class Student:
  def __init__(self, name, age, groupNumber):
    self.name = name
    self.age = age
    self.groupNumber = groupNumber
  def getName(self):
    return self.name
  def getAge(self):
    return self.age
  def getGroupNumber(self):
    return self.groupNumber
  def setNameAge(self, name, age):
    self.name = name
    self.age = age
  def setGroupNumber(self, groupNumber):
    self.groupNumber = groupNumber
student1 = Student("Miyo", 13, "6A")
student2 = Student("Asahi", 13, "WEB1A")
student3 = Student("Mahiro", 13, "SIB2A")
student4 = Student("Mihari", 18, "P4B")
student5 = Student("Kaede", 20, "11B")
print(f"Student 1 - Name: = {student1.getName()}, Age = {student1.getAge()}, Group = {student1.getGroupNumber()}")
print(f"Student 2 - Name = {student2.getName()}, Age = {student2.getAge()}, Group = {student2.getGroupNumber()}")
print(f"Student 3 - Name = {student3.getName()}, Age = {student3.getAge()}, Group = {student3.getGroupNumber()}")
print(f"Student 4 - Name = {student4.getName()}, Age = {student4.getAge()}, Group = {student4.getGroupNumber()}")
print(f"Student 5 - Name = {student5.getName()}, Age = {student5.getAge()}, Group = {student5.getGroupNumber()}")

#Ex 2
class Math:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def addition(self):
    result = self.a + self.b
    print(f"Add: {self.a} + {self.b} = {result}")
  def subtraction(self):
    result = self.a - self.b
    print(f"Subtraction: {self.a} - {self.b} = {result}")
  def multiplication(self):
    result = self.a * self.b
    print(f"Multiply: {self.a} * {self.b} = {result}")
  def division(self):
    if self.b != 0:
      result = self.a / self.b
      print(f"Divide: {self.a} / {self.b} = {result}")
    else:
      print("You can't divide by 0")
problem = Math(4, 10)
problem.addition()
problem.multiplication()
problem.division()
problem.subtraction()

#Ex 3
class Car:
  def __init__(self, color, type, year):
    self.color = color
    self.type = type
    self.year = year
    self.is_running = False
  def start(self):
    if not self.is_running:
      self.is_running = True
      print("The car is on")
    else:
      print("The car is ALREADY on")
  def stop(self):
    if self.is_running:
      self.is_running = False
      print("The car is off")
    else:
      print("The car is ALREADY off")
  def set_year(self, year):
    self.year = year
    print(f"The car production year is set to {year}")
  def set_type(self, car_type):
    self.type = type
    print(f"The car type is set to {car_type}")
  def set_color(self, color):
    self.color = color
    print(f"The car color is set to {color}")
my_car = Car("Blue", "Tesla", 2000)
my_car.start()
my_car.stop()
my_car.set_year(2015)
my_car.set_type("SportCar")
my_car.set_color("White")

#Ex 4
class BankAccount:
  def __init__(self, name, balance):
    self.__name = name
    self.__balance = balance
  def get_balance(self):
    return self.__balance
  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__balance:
      self.__balance -= amount
  def display(self):
    print(f"Owner: {self.__name}")
    print(f"Balance: ${self.__balance:.2f}")
  def set_name(self, new_name):
    self.__name = new_name
  def close_account(self):
    self.__balance = 0
if __name__ == "__main__":
  account = BankAccount("RynnLee", 20041208)
  account.display()
  account.deposit(1200)
  account.withdraw(1300)
  account.display()
  account.set_name("DaudAttano")
  account.display()
  account.close_account()
  account.display()