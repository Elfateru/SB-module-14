def my_zip(*args):
    args = list(map(list, args))
    length = min(len(elem) for elem in args)
    tpl_list = [tuple(struct[i] for struct in args) for i in range(length)]
    return tpl_list


a = [{"x": 4}, "b", "z", "d"]
b = (10, {20, }, [30], "z")
print(my_zip(a, b))  # -> [({‘x’: 4}, 10), (‘b’, {20}), (‘z’, [30]), (‘d’, ‘z’)]

a = [1, 2, 3, 4, 5]
b = {1: "s", 2: "q", 3: 4}
x = (1, 2, 3, 4, 5)
print(my_zip(a, b, x))  # -> [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
