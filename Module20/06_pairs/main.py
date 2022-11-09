import random

original_list = [random.randint(0, 10) for _ in range(11)]
print(original_list)



new_list = []
temp = 0
for i in range(5):
    new_list.append((original_list[i + temp], original_list[i + 1 + temp]))
    temp += 1
if len(original_list) % 2 != 0:
    new_list.append((original_list[i + temp], original_list[i + 1 + temp]))
print(new_list)


new_list = zip(original_list[::2], original_list[1::2])
print(new_list)
