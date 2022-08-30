amount_skates = int(input('Кол-во коньков: '))
skates = []
people = []
count = 0
for sizes in range(1, amount_skates + 1):
    print(f'Размер {sizes}-й пары: ', end='')
    size = int(input())
    skates.append(size)
    skates.sort()

amount_people = int(input('\nКол-во людей: '))
for sizes in range(1, amount_people + 1):
    print(f'Размер ноги {sizes}-го человека: ', end='')
    size = int(input())
    people.append(size)
    people.sort()

for num in people:
    for match in range(len(skates)):
        if skates[match] >= num:
            skates.remove(skates[match])
            count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
