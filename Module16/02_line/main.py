first_class = []
second_class = []
line = []

for student in range(160, 177, 2):
    first_class.append(student)
for student in range(162, 181, 3):
    second_class.append(student)

line.extend(first_class)
line.extend(second_class)

line.sort()
print(line)
