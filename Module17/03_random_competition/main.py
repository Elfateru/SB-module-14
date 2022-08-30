import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_win = [team_1[num] if team_1[num] > team_2[num]
            else team_2[num]
            for num in range(20)]

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', team_win)