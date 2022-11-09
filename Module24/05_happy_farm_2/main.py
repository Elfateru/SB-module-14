class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        print(self)

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def __str__(self):
        return 'Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        )


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        if self.potatoes:
            print('\nКартошка проростает!')
            for potato in self.potatoes:
                potato.grow()
        else:
            print('На грядке нет картошки')

    def are_all_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('\nВся картошка на грядке созрела. Можно собирать.\n')
            return True
        else:
            print('\nКартошка ещё не созрела!\n')

    def print_all_states(self):
        for potato in self.potatoes:
            print(potato)


class Gardener:

    def __init__(self, name, potato_harvest=0):
        self.name = name
        self.potato_harvest = potato_harvest

    def care_of_the_garden(self, garden_bed):
        garden_bed.grow_all()

    def harvest(self, garden_bed):
        if garden_bed.are_all_ripe():
            self.potato_harvest += len(garden_bed.potatoes)
            print('Урожай на грядке собран садовником {}\nВсего: {} шт.'.format(self.name, self.potato_harvest))
            garden_bed.potatoes = []


g = Gardener('Vasya')
p_g_1 = PotatoGarden(5)
p_g_2 = PotatoGarden(1)
g.care_of_the_garden(p_g_1)
g.care_of_the_garden(p_g_1)
g.harvest(p_g_1)
g.care_of_the_garden(p_g_1)
g.harvest(p_g_1)
g.care_of_the_garden(p_g_1)
g.care_of_the_garden(p_g_2)
g.care_of_the_garden(p_g_2)
g.care_of_the_garden(p_g_2)
g.harvest(p_g_2)
