def number_summ(num):
    number = 0
    while num > 0:
        temp = num % 10
        number += temp
        num //= 10
    return number

def number_count(num):
    number = 0
    while num > 0:
        num //= 10
        number += 1
    return number

number = int(input('Введите число: '))

num_summ = number_summ(number)
num_count = number_count(number)

difference = abs(num_summ - num_count)

print('Сумма чисел: ', num_summ)
print('Количество цифр в числе: ', num_count)
print('Разность суммы и количества цифр: ', difference)