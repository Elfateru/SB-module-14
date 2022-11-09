site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, max_dep, cur_dep=1):
    if key in struct and max_dep > 0:
        return struct[key]
    cur_dep += 1
    if cur_dep <= max_dep:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                if key in sub_struct:
                    result = sub_struct[key]
                    return result
                else:
                    result = find_key(sub_struct, key, max_dep, cur_dep)
                    if result:
                        return result
    else:
        return None


user_key = input('Введите искомый ключ: ')
depth_question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if depth_question == 'y':
    depth = int(input('введите максимальную глубину: '))
    value = find_key(site, user_key, depth)
else:
    value = find_key(site, user_key, 1000)
print(value)
