print ('Долгов Андрей П4Б / Rynn Lee')

#Ex1
Arr1 = [1,3,5,7,9,0,8,6,4,2]
print('Наименьшее число: ', min(Arr1), '\nНаибольшее число: ', max(Arr1))

#Ex2
Arr2 = ['Reject', 'python', 'embrace', 'sane', 'programming', 'languages']
print(Arr2.sort())

#Ex3
Arr31 = [1, 2, 3, 4, 5]
Arr32 = [3, 4, 5, 6, 7]
print(list(Arr1 and Arr2))

#Ex4
Touple = ('a dictionary', 'called','its', 'that', 'fact', 'the', 'accept', 'gonna', 'not', 'Still')
ReversedTouple = ''
for i in reversed(Touple):
  ReversedTouple += ' ' + i
print(ReversedTouple)

#Ex5
def ToupleLength(touple):
  return len(touple)

Tuple2 = (1,3,5,7,9,0,8,6,4,2)
print('Touple length:', ToupleLength(Tuple2))

#Ex6
Arr61 = {1,2,5,7,9,0}
Arr62 = {3,5,6,7,8,9}

if Arr61.issubset(Arr62):
  print('Arr62 is a subset of Arr61')
else:
  print('Arr62 is NOT a subset of Arrr61')

#Ex7
def Unique(Arr1, Arr2):
  return Arr1.union(Arr2)

Arr71 = {1,2,3,4,5,6}
Arr72 = {3,4,5,6,7,8,9}
print("Unique values: ", Unique(Arr71, Arr72))

#Ex8
capitals = {
  'Kazakhstan': 'Astana',
  'Russia': 'Moscow',
  'Canada': 'Toronto',
  'USA': 'New York',
  'Ukraine': 'Kiev',
  'Japan': 'Tokyo'
}

def find(country):
  if country in capitals:
    return capitals[country]
  else:
    return 'Capital not found'

country = input('Choose a country: ')
print(f'Country {country}: {find(country)}')

#Ex9
def keys(dict):
  return list(dict.keys())

thisIsAnObject = {
  'Name': 'RynnLee',
  'Language': 'JS',
  'HatesPython': True,
  'Age': 18
}

print('Keys:', keys(thisIsAnObject))

#Ex10
inventory = {
  'NeedForSpeed': 25,
  'RedAlert2': 16,
  'Stronghold': 10,
  'Osu': 14,
  'Phasmophobia': 32,
  'Transformice': 41,
}

def sell(item, amount):
  if not item in inventory:
    return (f'No such items in the inventory: {item}')
  if not inventory[item] >= amount:
    return (f'No enough items in the inventory: {item}')
  
  inventory[item] -= amount
  return (f'Sold {amount} of: {item}')

print(sell('NeedForSpeed', 20))
print(sell('RedAlert2', 20))
print(sell('L4D2', 20))
print(sell('Osu', 20))
print(sell('Phasmophobia', 20))
print(sell('Transformice', 20))
print(sell('GTA', 20))
print(sell('Stronghold', 20))