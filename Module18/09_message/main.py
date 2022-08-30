msg = input('Сообщение: ')
temp = ''
new_str = ''
for sym in msg:
    if sym.isalpha():
        temp += sym
    else:
        temp = temp[::-1]
        new_str += temp + sym
        temp = ''

print(new_str)
