from random import randint


class Man:

    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self):
        self.satiety += 10
        self.house.food -= 10

    def work(self):
        self.satiety -= 10
        self.house.money += 10

    def play(self):
        self.satiety -= 10

    def go_to_shop(self):
        self.house.food += 30
        self.house.money -= 30


class House:

    def __init__(self, food=0, money=0):
        self.food = food
        self.money = money

    def __str__(self):
        return 'Food: {}\nMoney: {}'.format(self.food, self.money)


def action_logic(mates, cube):
    for man in mates:
        if man.satiety < 0:
            print(man.name, 'умер от голода :(')
            return 1
        elif man.satiety < 20 and man.house.food >= 10:
            man.eat()
        elif house_1.food < 10 and man.house.money >= 30:
            man.go_to_shop()
        elif man.house.money < 50:
            man.work()
        elif cube == 1:
            man.work()
        elif cube == 2 and man.house.food >= 10:
            man.eat()
        else:
            man.play()


house_1 = House()
man_1 = Man('Vaysa', house_1)
man_2 = Man('Masha', house_1)
roommates = [man_1, man_2]

for day in range(1, 366):
    magic_cube = randint(1, 6)
    if action_logic(roommates, magic_cube):
        break
    print(house_1.money)
