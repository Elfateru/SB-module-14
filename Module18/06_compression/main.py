def comression(text):
    count = 1
    compressed_text = []
    for index in range(len(text)):
        if text[index] == text[index + 1:index + 2]:
            count += 1
            continue
        compressed_text.append(text[index] + str(count))
        count = 1
    return compressed_text


new_str = input('Введите строку: ')
comressed_list = comression(new_str)
print('Закодированная строка: {}'.format(''.join(comressed_list)))
