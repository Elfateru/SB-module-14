def least_divisor(num):
    for count in range(2, num):
        if num % count == 0:
            return count
    return num


number = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы: ', least_divisor(number))