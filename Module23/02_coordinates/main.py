import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


def f3(name_file):
    with open(name_file, 'r') as file:
        for i_line in file:
            try:
                num_list = i_line.split()
                res_1 = f(int(num_list[0]), int(num_list[1]))
                res_2 = f2(int(num_list[0]), int(num_list[1]))
                number = random.randint(0, 100)
                with open('result.txt', 'w') as file_2:
                    my_list = sorted([str(res_1), str(number), str(res_2)])
                    file_2.write(' '.join(my_list))
            except Exception as exc:
                print('Что-то пошло не так    ', exc)


f3('coordinates.txt')
