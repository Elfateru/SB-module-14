balance = []
friends_amnt = int(input('Кол-во друзей: '))
iou_amnt = int(input('Кол-во расписок: '))
for _ in range(friends_amnt):
    balance.append(0)

for num in range(iou_amnt):
    print(f'{num + 1}-я расписка')
    lender = int(input('Кому: '))
    borrower = int(input('От кого: '))
    while lender == borrower:
        print('\nНельзя взять в долг у самого себя!')
        print(f'\n{num + 1}-я расписка')
        lender = int(input('Кому: '))
        borrower = int(input('От кого: '))
    temp_sum = int(input('Сколько: '))
    balance[lender - 1] -= temp_sum
    balance[borrower - 1] += temp_sum

print('\nБаланс друзей: ')
for friend in range(len(balance)):
    print(f'{friend + 1}: {balance[friend]}')
