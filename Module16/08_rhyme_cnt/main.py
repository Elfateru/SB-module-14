num = int(input('Кол-во человек: '))
counting = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {counting}-й человек')
members = list(range(1, num + 1))
start = 0
print(members)

while len(members) > 1:
    print('\nТекущий круг людей:', members)
    print('Начало счёта с номера', members[start])
    start = (start + counting) % len(members)
    if start == 0:
        print('Выбывает человек под номером', members[-1])
        members.pop(-1)
        start = 0
    else:
        print('Выбывает человек под номером', members[start - 1])
        members.pop(start - 1)
        start -= 1
print('\nОстался человек под номером', members[0])