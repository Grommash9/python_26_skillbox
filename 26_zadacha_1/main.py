from square_c import SquareCreator


def geterator_func(q: int):
    counter = 0
    while counter < q:
        yield counter ** 2
        counter += 1


n = int(input('До какого числа генерировать последовательность?'))

class_iterator = SquareCreator(n)

print('\n\nВывод полученный с класса итератора')
for items in class_iterator:
    print(items)

sqare_list = geterator_func(n)

print('\n\nВывод полученный с функции гетератора')
for numbers in sqare_list:
    print(numbers)

second_square_list = [x ** 2 for x in range(0, n)]
print('\n\nВывод полученный с выражения гетератора')
for values in second_square_list:
    print(values)
