def number_finder(some_list_1: list, some_list_2: list):
    for x in some_list_1:
        for y in some_list_2:
            result = x * y
            print(x, y, result)
            yield result


list_1 = [2, 5, 7, 10]

list_2 = [3, 8, 4, 9]

to_find = 56


for product_of_multiplication in number_finder(list_1, list_2):
    if product_of_multiplication == to_find:
        print('Нашел')
        break
