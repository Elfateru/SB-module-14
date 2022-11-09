def sum_func(*args):
    summ = 0
    for i in args:
        if isinstance(i, list):
            for lst in i:
                summ += sum_func(lst)
        else:
            summ += i
    return summ


print(sum_func([[1, 2, [3]], [1], 3]))
print(sum_func(1, 2, 3, 4, 5))
