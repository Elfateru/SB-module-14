def caesar_cipher(text, shift, alphabet):
    new_list = [(alphabet[(alphabet.index(sym) + shift) % len(alphabet)]
                 if sym in alphabet else sym) for sym in text]
    string = ''.join(new_list)
    return string


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

cipher_text = caesar_cipher(text, shift, alphabet)

print('Зашифрованное сообщение:', cipher_text)
