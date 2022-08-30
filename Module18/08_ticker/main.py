def new_func(s_str, f_str):
    for count in range(len(f_str) - 1):
        s_str = s_str[-1] + s_str[:-1]
        if f_str == s_str:
            return count + 1
    return False


first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
if first_str == second_str:
    print('Первая строка идентична второй')
elif len(first_str) != len(second_str):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    shift = new_func(second_str, first_str)
    if shift:
        print('Первая строка получается из второй со сдвигом {}.'.format(shift))
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
