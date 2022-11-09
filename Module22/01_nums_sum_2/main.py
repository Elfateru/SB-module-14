read_file = open('numbers.txt', 'r')
num_sum = 0

for i_line in read_file:
    for i_sym in i_line:
        if i_sym.isdigit():
            num_sum += 1
read_file.close()

write_file = open('answer.txt', 'w')
write_file.write(str(num_sum))
write_file.close()
