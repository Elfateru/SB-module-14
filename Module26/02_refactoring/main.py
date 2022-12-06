def func(l_1, l_2):
    for x in l_1:
        for y in l_2:
            print(x, y, x * y)
            yield x * y


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for i in func(list_1, list_2):
    if i == to_find:
        print('Found!!!')
        break
