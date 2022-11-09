def sum_func(line, opetation):
    line_list = line.split()
    try:
        if line_list[1] not in opetation:
            raise TypeError
        elif len(line_list) != 3:
            raise IndexError
        elif not line_list[0].isdigit() or not line_list[2].isdigit():
            raise TypeError
        else:
            return eval(line)
    except Exception:
        if input(f'Обнаружена ошибка в строке: {line.rstrip()} Хотите исправить? ').lower() == 'да':
            line = input('Введите исправленную строку:')
            result = sum_func(line, opetation)
        else:
            result = 0
    return result


math_operation = ['+', '-', '*', '/', '//', '%']
result = 0
try:
    with open('calc.txt', 'r') as file:
        for i_line in file:
            result += sum_func(i_line, math_operation)
    print(result)
except FileNotFoundError:
    print('Файл не найден')
