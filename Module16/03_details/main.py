shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count = 0
price = 0
detail = input('Название детали: ')
for index in range(len(shop)):
    if shop[index][0] == detail:
        count += 1
        price += shop[index][1]

print('Кол-во деталей -', count)
print('Общая стоимость -', price)


