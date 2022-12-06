# класс итератор
class NumIterator:
    def __init__(self, end):
        self.count = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.end:
            return self.count ** 2
        else:
            raise StopIteration


# функция генератор
def square_gen(nums):
    for n in range(1, nums+1):
        yield n ** 2


number = int(input('Введите число: '))

# генераторное выражение
square_nums = (n ** 2 for n in range(1, number + 1))
