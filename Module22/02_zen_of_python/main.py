file = open('zen.txt', 'r', encoding='utf8')
line_list = file.readlines()
line_list.insert(-1, '\n')

file.close()
print(line_list)
for reverse_text in line_list[::-1]:
    print(reverse_text, end='')
