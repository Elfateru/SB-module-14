text = input('Введите строку: ')

btwn_text = text[text.rindex('h') - 1:text.index('h'):-1]

print('Развернутая последовательность между первым и последним h:', btwn_text)
