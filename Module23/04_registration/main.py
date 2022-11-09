def data_check(data):
    data = data.split()
    if len(data) != 3:
        raise IndexError('Не присутствуют все три поля\n')
    elif not data[0].isalpha():
        raise NameError('Поле имени содержит НЕ только буквы\n')
    elif '@' not in data[1] or '.' not in data[1]:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)\n')
    elif not data[2].isdigit() or int(data[2]) > 100 or 9 > int(data[2]):
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99\n')


try:
    with open('registrations.txt', 'r', encoding='utf8') as reg_file:
        with open('registrations_good.txt', 'w', encoding='utf8') as reg_good:
            with open('registrations_bad.txt', 'w', encoding='utf8') as reg_bad:
                for i_line in reg_file:
                    try:
                        data_check(i_line)
                        reg_good.write(i_line)
                    except Exception as error:
                        reg_bad.write(f'{i_line.rstrip()}        {error}')

except FileNotFoundError:
    print('Файл не найден')
