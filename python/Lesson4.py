print("Долгов Андрей П4Б / Rynn Lee")
#Ex 1
def tpl_sort(Arr):
  if all(isinstance(i, int) for i in Arr):
    return tuple(sorted(Arr))
  else:
    return Arr
Arr = (1,3,6,3,7,3,56)
print(tpl_sort(Arr))
Arr2 = ("Text", 1.2, 435, 43)
print(tpl_sort(Arr2))

#Ex 2
def slicer(Arr, i):
  index1 = Arr.index(i) if i in Arr else None
  index2 = None
  if index1 is not None:
    try:
      index2 = Arr.index(i, index1 + 1)
    except ValueError:
      pass
  if index1 is not None and index2 is not None:
    return Arr[index1:index2 + 1]
  elif index1 is not None:
    return Arr[index1:]
  else:
    return ()
Arr = (1,3,5,7,9,0,2,4,5,6,7,8,9)
print(slicer(Arr, 2))
print(slicer(Arr, 7))
print(slicer(Arr, 4))

#Ex 3
def sieve(Arr):
  return tuple(reversed(list(set(Arr))))
Arr = [1,2,3,4,5,6,7,8,9,0]
print(sieve(Arr))

#Ex 4
def del_from_tuple(Arr, i):
  if i in Arr:
    return Arr[:Arr.index(i)] + Arr[Arr.index(i) + 1:]
  else:
    return Arr
Arr = (1, 2, 3, 4, 5, 6, 7)
print(del_from_tuple(Arr, 3))
print(del_from_tuple(Arr, 6345645))

#Ex 5
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])
students = (
  Student('Andrey', 18, 100, 'Almaty'),
  Student('Anna', 15, 90, 'Idk'),
  Student('Someone', 17, 90, 'Paris'),
  Student('Maria', 22, 85, 'Toronto'),
)
def good_students(students):
  score = sum(student.grade for student in students)
  minScore = score / len(students)
  good_students = [student.name for student in students if student.grade >= minScore]
  if good_students:
    print(f"Students {', '.join(good_students)} studying well this semester")
  else:
    print("There are no students that are studying well")
good_students(students)

#Ex 6
def to_set(mystring):
  if isinstance(mystring, str):
    res = set(mystring)
  elif isinstance(mystring, list):
    res = set(mystring)
  else:
    raise ValueError("Input should be a string or an array of numbers")
  size = len(res)
  return res, size
teststring = "SomeTextToTest"
Arr = [1,2,3,4,5,6,7,8,9,0]
Arra, ArraPower = to_set(teststring)
print("Array:", Arra)
print("ArrayPower:", ArraPower)
Arra, ArraPower = to_set(Arr)
print("Power:", Arra)
print("ArrayPower:", ArraPower)

#Ex 7
def hashing(i):
  try:
    hash(i)
    return True
  except TypeError:
    return False
def list_to_set(mylist):
  result = set()
  for i in mylist:
    if hashing(i):
      result.add(i)
  return result
Arr = [1,2,3,4,5,6,"Something","again",[1,2,3,4,5],(1,2,3,4,5)]
print(list_to_set(Arr))

#Ex 8
def to_dict(lst):
  result = {}
  for i in lst:
    result[i] = i
  return result
Arr = ["Still", "Not", "Gonna", "Call", "It", "List"]
print(to_dict(Arr))

#Ex 9
def biggest_dict(**kwargs):
  obj = {'first_one': 'we can do it'}
  obj.update(kwargs)
  return obj
print(biggest_dict(second = 'secondd', third = 'thirdd'))