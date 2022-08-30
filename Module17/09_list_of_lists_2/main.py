nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [num for each_list in nice_list
            for each_list_2 in each_list
            for num in each_list_2]

print('Ответ:', new_list)