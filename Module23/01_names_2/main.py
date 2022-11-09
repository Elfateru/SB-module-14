with open('people.txt', 'r', encoding='utf8') as file:
    line_count = 0
    total_chars = 0
    for i_line in file:
        try:
            line_count += 1
            clear_line = i_line.rstrip()
            if len(clear_line) < 3:
                raise IndexError('Ошибка: менее трёх символов в строке {number}.'.format(number=line_count))
        except Exception as exc:
            print(exc)
        total_chars += len(clear_line)
print('Общее кол-во символов: {}'.format(total_chars))

