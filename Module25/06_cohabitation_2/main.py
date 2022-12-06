from random import randint


class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cats_food = 30
        self.dirt = 0
        self.total_money = 0
        self.total_food_eaten = 0
        self.total_bought_fur_coat = 0


class Husband:
    def __init__(self, home):
        self.__name = 'Vasya'
        self.__satiety = 30
        self.__happiness = 100
        self.__home = home

    def set_happiness(self):
        self.__happiness -= 10

    def eat(self):
        if self.__home.food >= 30:
            self.__home.food -= 30
            self.__satiety += 30
            self.__home.total_food_eaten += 30
        else:
            self.__satiety += self.__home.food
            self.__home.total_food_eaten += self.__home.food
            self.__home.food = 0

    def play(self):
        self.__happiness += 20
        self.__satiety -= 10

    def work(self):
        self.__home.money += 150
        self.__home.total_money += 150
        self.__satiety -= 10

    def pet_the_cat(self):
        self.__happiness += 5
        self.__satiety -= 10

    def day_of_life(self):
        if self.__home.total_money < 350:
            if self.__satiety > 19 and self.__happiness > 29:
                self.work()
            elif self.__satiety < 20:
                self.eat()
            elif self.__happiness < 30:
                if randint(1, 2) == 1:
                    self.play()
                else:
                    self.pet_the_cat()
        elif self.__satiety < 20 and self.__home.food > 0:
            self.eat()
        else:
            if randint(1, 2) == 1:
                self.play()
            else:
                self.pet_the_cat()
        if self.__satiety <= 0 or self.__happiness < 10:
            print('Муж скончался')
            return True


class Wife:
    def __init__(self, home):
        self.__name = 'Asya'
        self.__satiety = 30
        self.__happiness = 100
        self.__home = home

    def set_happiness(self):
        self.__happiness -= 10

    def eat(self):
        if self.__home.food >= 30:
            self.__home.food -= 30
            self.__satiety += 30
            self.__home.total_food_eaten += 30
        else:
            self.__satiety += self.__home.food
            self.__home.total_food_eaten += self.__home.food
            self.__home.food = 0

    def buy_food(self):
        self.__home.food += 60
        self.__home.money -= 60
        if self.__home.cats_food < 10:
            self.__home.cats_food += 20
            self.__home.money -= 20
        self.__satiety -= 10

    def buy_fur_coat(self):
        if self.__home.total_money >= 350:
            self.__home.money -= 350
            self.__happiness += 60
            self.__satiety -= 10
            self.__home.total_bought_fur_coat += 1

    def cleaning(self):
        if self.__home.dirt > 100:
            self.__home.dirt -= 100
        else:
            self.__home.dirt = 0
        self.__satiety -= 10

    def pet_the_cat(self):
        self.__happiness += 5
        self.__satiety -= 10

    def day_of_life(self):
        if self.__satiety > 19 and self.__happiness > 29:
            if self.__home.food < 30 and self.__home.money >= 80:
                self.buy_food()
            else:
                self.cleaning()
        elif self.__satiety < 20 and self.__happiness > 29:
            if self.__satiety >= self.__happiness - 10 and self.__home.money >= 350:
                self.buy_fur_coat()
            elif self.__home.food > 0:
                self.eat()
            else:
                self.pet_the_cat()
        else:
            self.pet_the_cat()
        if self.__satiety <= 0 or self.__happiness < 10:
            print('Жена скончалась')
            return True


class Cat:
    def __init__(self, home, husband, wife):
        self.__name = 'Kot'
        self.__satiety = 30
        self.__home = home
        self.owner_1 = husband
        self.owner_2 = wife

    def get_satiety(self):
        return self.__satiety

    def sleep(self):
        self.__satiety -= 10

    def eat(self):
        if self.__home.cats_food >= 10:
            self.__home.cats_food -= 10
            self.__satiety += 20
        else:
            self.__satiety += self.__home.cats_food * 2
            self.__home.cats_food = 0

    def scratch_wallpaper(self):
        self.__satiety -= 10
        self.__home.dirt += 5
        self.owner_1.set_happiness()
        self.owner_2.set_happiness()

    def day_of_life(self):
        if self.get_satiety() < 21 and self.__home.cats_food > 0:
            self.eat()
        elif self.get_satiety() <= 0:
            print('Кот скончался')
            return True
        else:
            if randint(1, 2) == 1:
                self.sleep()
            else:
                self.scratch_wallpaper()


home = House()
husband = Husband(home)
wife = Wife(home)
cat = Cat(home, husband, wife)


for day in range(1, 366):
    if home.dirt > 90:
        husband.set_happiness()
        wife.set_happiness()
    h_check = husband.day_of_life()
    w_check = wife.day_of_life()
    c_check = cat.day_of_life()
    if h_check or w_check or c_check:
        print(f'Кто-то умер на {day} дне')
        break
    home.dirt += 10
print('За год было заработано: {}\nСъедено еды: {}\nКуплено шуб: {}'.format(
    home.total_money, home.total_food_eaten, home.total_bought_fur_coat
)
)
