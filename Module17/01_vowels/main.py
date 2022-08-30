vowels = 'уеёэоаыяию'
text = input('Введите текст: ')

list_vowels = [sym for sym in text if sym in vowels]

print('\nСписок гласных букв:', list_vowels)
print('Длина списка:', len(list_vowels))
