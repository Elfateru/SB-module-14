text = input('Введите строку: ')
word_long = max(text.split(), key=lambda x: len(x))
print('самое длинное слово: {}'.format(word_long))
print('Длина этого слова: {}'.format(len(word_long)))
