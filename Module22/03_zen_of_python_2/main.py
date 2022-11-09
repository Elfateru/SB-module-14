import os

word_count = 0
sym_count = dict()
line_count = 0
total_sym = 0

file = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r')
for i_line in file:
    line_count += 1
    word_count += len(i_line.split())
    for i_sym in i_line:
        if i_sym.isalpha():
            total_sym += 1
            if i_sym.lower() in sym_count:
                sym_count[i_sym.lower()] += 1
            else:
                sym_count[i_sym.lower()] = 1
file.close()

rare_sym = min(sym_count.items(), key=lambda x: x[1])[0]

print('Количество букв в файле:', total_sym)
print('Количество слов в файле:', word_count)
print('Количество строк в файле:', line_count)
print('Наиболее редкая буква:', rare_sym)
