def least_divisor(num):
    temp = 0
    for count in range(num, 1, -1):
        if num % count == 0:
            temp = count
    if temp == 0:
        temp = num
    return temp


number = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы: ', least_divisor(number))