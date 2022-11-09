import random


total_sum = 0
with open('out_file.txt', 'w') as file:
    while True:
        if total_sum < 777:
            number = int(input('Введите число: '))
            random_exception = random.randint(1, 13)
            if random_exception == 1:
                raise ValueError('Вас постигла неудача!')

            file.write(str(number) + '\n')
            total_sum += number
        else:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
            break
