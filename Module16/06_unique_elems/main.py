main_list = []
first_list = []
second_list = []

for nums in range(1, 4):
    print(f'Введите {nums}-е число для первого списка: ', end='')
    num = int(input())
    first_list.append(num)
for nums in range(1, 8):
    print(f'Введите {nums}-е число для второго списка: ', end='')
    num = int(input())
    second_list.append(num)

print('Первый список:', first_list)
print('Второй список:', second_list)

main_list.extend(first_list)
main_list.extend(second_list)
main_list = set(main_list)
print('Новый список с уникальными элементами:', list(main_list))