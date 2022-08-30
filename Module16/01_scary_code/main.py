main_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]
num_1 = 0
num_2 = 0

main_list.extend(second_list)
num_1 += main_list.count(5)

for _ in range(num_1):
    main_list.remove(5)

main_list.extend(third_list)
num_2 += main_list.count(3)

print('Результат работы программы:')
print('Кол-во цифр 5 при первом объединении:', num_1)
print('Кол-во цифр 3 при первом объединении:', num_2)
print('Итоговый список:', main_list)
