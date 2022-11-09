def is_prime(num):
    if num < 2:
        return False
    check = 2
    while num % check != 0:
        check += 1
    return num == check


def crypto(data):
    return [sym for i_index, sym in enumerate(data) if is_prime(i_index)]


data_1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_2 = 'О Дивный Новый мир!'
print(crypto(data_1))
print(crypto(data_2))
