def fib(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))

fib_num = fib(number)
print('Число:', fib_num)