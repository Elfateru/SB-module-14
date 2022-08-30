while True:
    password = input('Придумайте пароль: ')
    password_len = len(password)
    password_nums = len(list(filter(lambda x: x.isdigit(), password)))
    password_cap_letter = len(list(filter(lambda x: x.isupper(), password)))
    if password_len >= 8 and password_nums >= 3 and password_cap_letter >= 1:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз')
