def tpl_sort(data):
    for i in data:
        if not isinstance(i, int):
            return data
    return tuple(sorted(data))


new_tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(new_tpl))
