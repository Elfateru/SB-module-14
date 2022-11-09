def num_count(num):
    if num == 0:
        return 0
    num_count(num - 1)
    print(num)


num_input = int(input('Ввежите число: '))
num_count(num_input)