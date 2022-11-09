def players_dict(note):
    note_dict = dict()
    print('Записи (результат и имя):')
    for i_note in range(note):
        score, name = input(f'{i_note + 1}-я запись: ').split()
        score = int(score)
        if name in note_dict:
            if note_dict[name][0] < score:
                note_dict[name][0] = score
                note_dict[name][1] = i_note
        else:
            note_dict[name] = [score, i_note]
    print(list(note_dict.items()))
    return list(note_dict.items())

while True:
    players = int(input('Сколько записей вносится в протокол? '))
    if players >= 3:
        break

new_list = players_dict(players)
new_list.sort(key=lambda x: x[1][0] - x[1][1], reverse=True)

print('\nИтоги соревнований:')
for i_winner in range(3):
    print(f'{i_winner + 1}-е место.'
          f' {new_list[i_winner][0]} '
          f'({new_list[i_winner][1][0]})'
          )
