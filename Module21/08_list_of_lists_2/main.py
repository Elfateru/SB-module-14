nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def one_list(lst):
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return one_list(lst[0]) + one_list(lst[1:])
    return lst[:1] + one_list(lst[1:])


print(one_list(nice_list))
print(one_list(nice_list))


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(flatten(nice_list))
print(flatten(nice_list))