def func(disk, pin_1, pin_2, pin_3):
    if disk == 1:
        print(f'Переложить диск {disk} со стержня {pin_1} на {pin_3}')
    else:
        func(disk - 1, pin_1, pin_3, pin_2)
        print(f'Переложить диск {disk} со стержня {pin_1} на {pin_3}')
        func(disk - 1, pin_2, pin_1, pin_3)

num = int(input('Введите кол-во дисков: '))

func(num, 1, 2, 3)
