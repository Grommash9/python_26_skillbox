class SquareCreator:

    def __init__(self, n: int):
        self.curent_number = -1
        self.__n = self.total_numbers_set(n)

    def __iter__(self):
        return self

    def __next__(self):
        self.curent_number += 1
        if self.curent_number < self.__n:
            return self.curent_number ** 2
        else:
            raise StopIteration

    def total_numbers_set(self, n: int) -> int:
        if n > 0 and isinstance(n, int):
            return n
        else:
            raise ValueError('Конечное значние должно быть больше нуля и целым числом')