def slicer(data, new_num):
    count = 0
    for i_index, sym in enumerate(data):
        if sym == new_num:
            count += 1
            if count == 1:
                start_index = i_index
                print(start_index, 'start')
            if count == 2:
                stop_index = i_index
                print(stop_index, 'stop')
                break
    if count < 2:
        return tuple()
    else:
        return data[start_index:stop_index + 1]


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
