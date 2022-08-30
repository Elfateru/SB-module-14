file_name = input('Название файла: ')
spec_sym = '@№$%^&\*()'
if file_name.endswith('.txt') or file_name.endswith('.docx'):
    if file_name[0] not in spec_sym:
        print('Файл назван верно.')
    else:
        print('Ошибка: название начинается на один из специальных символов.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')