first_tour = open('first_tour.txt', 'r')
file_list = []
for i_line in first_tour:
    if i_line[-1:] == '\n':
        file_list.append(i_line[:-1])
    else:
        file_list.append(i_line)
first_tour.close()

num_K = file_list.pop(0)

second_tour_list = []
for i_player in file_list:
    i_player = i_player.split()
    if int(i_player[2]) > int(num_K):
        temp_player = i_player[1][0] + '. ' + i_player[0] + ' ' + i_player[2]
        second_tour_list.append(temp_player.split())

sorted_players = sorted(second_tour_list, key=lambda x:int(x[2]), reverse=True)

second_tour_text = f'{str(len(sorted_players))}\n'

num = 0
for i_elem in sorted_players:
    num += 1
    second_tour_text += str(num) + ') ' + ' '.join(i_elem) + '\n'
print(second_tour_text)

second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(second_tour_text)
second_tour_file.close()