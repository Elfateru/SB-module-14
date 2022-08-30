available_menu = input('Доступное меню: ')
current_menu = ', '.join(available_menu.split(';'))

print('На данный момент в меню есть: {menu}'.format(menu=current_menu))
