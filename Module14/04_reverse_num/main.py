def rev(num):
    num = int(num)
    number = num % 10
    num //= 10
    while num > 0:
        number = (number*10) + num % 10
        num //= 10
    return str(number)

def reverse_num(num):
    flag = True
    number_1 = ''
    number_2 = ''
    for i in str(num):
        if i == '.':
            flag = False
            continue
        if flag is True:
            number_1 += i
        else:
            number_2 += i
    number_1 = rev(number_1)
    number_2 = rev(number_2)
    digit = number_1 + '.' + number_2
    digit = float(digit)
    return digit

first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))

first_num = reverse_num(first_num)
second_num = reverse_num(second_num)
print('\nПервое число наоборот: ', first_num)
print('Ворое число наоборот: ', second_num)

summ = first_num + second_num
print('Сумма: ', summ)