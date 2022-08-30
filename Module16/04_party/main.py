guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек', guests)
    move = input('Гость пришел или ушёл? ')
    if move == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя: ')
    if move == 'пришёл':
        if len(guests) < 6:
            print(f'Привет, {name}!')
            guests.append(name)
        else:
            print(f'Прости, {name}, но мест нет.')
    elif move == 'ушёл':
        print(f'Пока, {name}')
        guests.remove(name)