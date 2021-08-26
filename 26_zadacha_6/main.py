from new_list import NewList
import ctypes
from new_list import ListElement

a = NewList(0, 1, 5, 3, 3, 5, 98, 65, 101, 9, 10)

print('Создали список')
for elem in a:
    print(elem, end=' ')


a.append(121)
print('\nДобавили элемент')
for elem in a:
    print(elem, end=' ')

a.remove(1)
print('\nУдалили элемент')
for elem in a:
    print(elem, end=' ')

print('\nПолучаем гет')
print(a.get(1))

a.append(23)
a.append(2313)
a.append(2123)
a.append(213)

print('\nДобавили элемент')
for elem in a:
    print(elem, end=' ')

print('\nПолучаем гет')
print(a.get(14))

