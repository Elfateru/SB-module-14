family_dict = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова','Алина'): 34,
    ('Сидоров', 'Павел'): 10
}

surname_order = input('Введите фамилию: ')

for key, val in family_dict.items():
    if key[0][:-1] == surname_order or key[0] == surname_order or key[0] == surname_order[:-1]:
        print(key[0], key[1], val)