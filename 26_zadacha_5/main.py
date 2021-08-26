import os


def line_counter(some_dir: str):
    os.chdir(some_dir)
    total_counter = 0
    for elements in os.listdir(some_dir):
        counter = 0
        if os.path.basename(elements).endswith('.py'):
            with open(os.path.basename(elements), 'r') as current_python_file:
                for line in current_python_file:
                    for symbols in line:
                        if symbols.isalpha() or symbols.isdigit() and not symbols == '#':
                            counter += 1
                            break
            total_counter += counter
            yield f'В файле {os.path.basename(elements)} {counter} строчек кода'

    yield f'Всего строчек кода в файлах этой директории: {total_counter}'


path = input('Введите путь к директории, которая содержит питон файлы')
#path = 'C:/'


for results in line_counter(path):
    print(results)

