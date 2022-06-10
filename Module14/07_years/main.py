def num_match(start, stop):
    for count in range(start, stop+1):
        temp = count
        num_1 = count % 10
        count //= 10
        num_2 = count % 10
        count //= 10
        num_3 = count % 10
        count //= 10
        num_4 = count % 10
        if (num_1 == num_2 and num_1 == num_3) or (num_1 == num_3 and num_1 == num_4):
            print(temp)
            pass
        elif (num_2 == num_1 and num_2 == num_3) or (num_2 == num_3 and num_2 == num_4):
            print(temp)
            pass
        elif (num_3 == num_1 and num_3 == num_2) or (num_3 == num_2 and num_3 == num_4):
            print(temp)
            pass
        elif (num_4 == num_1 and num_4 == num_2) or (num_4 == num_2 and num_4 == num_3):
            print(temp)
            pass

start = int(input('Введите первый год: '))
stop = int(input('Введите второй год: '))
if len(str(start)) == 4 and len(str(stop)) == 4:
    print(f'\nГоды от {start} до {stop} с тремя одинаковыми цифрами: ')

    num_match(start, stop)
