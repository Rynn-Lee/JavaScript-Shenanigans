print("Долгов Андрей П4Б - Rynn Lee")
# Ex 1
try:
  a = input("Num: ")
  print("Num:", a)
except ValueError:
  print("Error: Type number!")

# Ex 2
try:
  a = float(input("Num 1: "))
  b = float(input("Num 2: "))
  print("Result:", a / b)
except ZeroDivisionError:
  print("Error: Cannot divide by zero")

# Ex 3
try:
  with open("text1.txt", "r") as file:
    res = file.read()
  print("File contains: ", res)
except FileNotFoundError:
  print("Error: File doesn't exist")

# Ex 4
try:
  a = input("Num: ")
  print("Num:", float(a))
except ValueError:
  print("Error: your character is not a number")

# Ex 5
import sqlite3
try:
  conn = sqlite3.connect("db.db")
  cursor = conn.cursor()
  conn.close()
except sqlite3.Error as exception:
  print("Cannot connect to db:", exception)

# Ex 6
try:
  a = input("Num 1: ")
  b = input("Num 2: ")
  print("Result:", a / b)
except ZeroDivisionError:
  print("Error: number needed!")

# Ex 7
Arr = [4, 7, 3]
try:
  print("Value:", Arr[5])
except IndexError as exception:
  print("Error:", exception)

# Ex 8
from datetime import datetime
date = "2020-10-20"
try:
  print("Date:", datetime.strptime(date, "%b-%m-%d"))
except ValueError as exception:
  print("Error: Wrong date format -", exception)

# Ex 9
try:
  with open("text2.txt", "w") as file:
    file.write("No one calls array as heckin lists!")
except PermissionError as exception:
  print("Error: not enough permissions to write", exception)

# Ex 10
obj = {"key1": "key2", "key3": "key4"}
try:
  print("Value: ", obj["key5"])
except KeyError as exception:
  print("Error: key not found!", exception)

# Ex 11
try:
  with open("text3.txt", "r") as file:
    res = file.read()
  print("File:", res)
except FileNotFoundError as exception:
  print("Error: File not found!", exception)

# Ex 12
Arr1 = (4, 7, 3)
try:
  print("Value:", Arr1[5])
except IndexError as exception:
  print("Error: Index is out of bounds", exception)

# Ex 13
try:
  a = float(input("Num 1: "))
  b = float(input("Num 2: "))
  if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    print("Result", a / b)
except ValueError as exception:
  print("Error:", exception)

# Ex 14
try:
  with open("text3.txt", "r") as file:
    res = file.read()
  print("File contains:", res)
except FileNotFoundError as exception:
  print("Error: File not found", exception)

# Ex 15
try:
  a = input("Num: ")
  print("Converted value:", float(a))
except ValueError as exception:
  print("Error: value is not a float number", exception)