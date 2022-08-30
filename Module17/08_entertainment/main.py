import random


def throws(stick, throw):
    sticks_list = ['I' for _ in range(stick)]
    for i in range(1, throw + 1):
        left_i = random.randint(1, stick)
        right_i = random.randint(left_i, stick)
        print(f'Бросок {i}. Сбиты палки с номера {left_i} по номер {right_i}')
        sticks_list = [sticks_list[i_index] if left_i - 1 > i_index or i_index > right_i - 1
                       else '.' for i_index in range(stick)]
    return sticks_list


sticks_total = int(input('Количество палок: '))
throws_total = int(input('Количество бросков: '))

sticks = throws(sticks_total, throws_total)

print('Результат:', sticks)
