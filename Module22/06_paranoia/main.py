import string

def cipher_shift(text, shift, alphabet):
    new_list = [(alphabet[(alphabet.index(sym) + shift) % len(alphabet)]
                 if sym in alphabet else sym) for sym in text]
    string = ''.join(new_list)
    return string


symbols = string.ascii_lowercase
new_text = ''
from_file = open('text.txt', 'r')
line_lvl = 0
for i_line in from_file:
    line_lvl += 1
    new_text += cipher_shift(i_line.lower(), line_lvl, symbols).title()
from_file.close()

cipher_file = open('cipher_text.txt', 'w')
cipher_file.write(new_text)
cipher_file.close()


