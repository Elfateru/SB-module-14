import random

numbers = int(input('Кол-во чисел в списке: '))
list_num = [random.randint(0, 2) for _ in range(numbers)]
print('Список до сжатия:', list_num)

list_num = [num for num in list_num if num]
print('Список после сжатия:', list_num)
