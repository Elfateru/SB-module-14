def calculating_math_func(data, data_dict={}):
    if data not in data_dict:
        result = 1
        for index in range(1, data + 1):
            result *= index
            data_dict[index] = result
    else:
        result = data_dict[data]
    result /= data ** 3
    result = result ** 10
    return result
