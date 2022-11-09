import os.path


def write_file(path, text):
    new_file = open(path, 'w', encoding='utf8')
    new_file.write(text)
    new_file.close()


def get_input_parameters():
    text = input('Введите строку: ')
    path = input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
    file = input('\nВведите имя файла: ') + '.txt'
    return  text, path, file


def path_gen(path):
    path = os.path.abspath(os.path.sep)
    for i_path in path_of_file:
        path = os.path.join(path, i_path)
    return path
def check_path_to_file(text, path, file):
    if not os.path.exists(path):
        print('Такого пути нет!')
    else:
        abs_path_to_file = os.path.abspath(os.path.join(path, file))
        if os.path.exists(abs_path_to_file):
            ask_for_write = input('Вы действительно хотите перезаписать файл? ').lower()
            if ask_for_write == 'да':
                write_file(abs_path_to_file, text)
        else:
            write_file(abs_path_to_file, text)
        print('Файл успешно сохранён')

new_text, path_of_file, file_name = get_input_parameters()  # Получаем входные данные
abs_path = path_gen(path_of_file)  # Генерация запрашиваемого пути из списка
check_path_to_file(new_text, abs_path, file_name)  # Проверка пути к файлу и запись файла
