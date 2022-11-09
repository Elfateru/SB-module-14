import random


class Warrior:

    def __init__(self, unit, health=100):
        self.unit = unit
        self.health = health

    def strike(self):
        self.health -= 20


def who_attack(u_1, u_2):
    attacker = random.randint(1, 2)
    if attacker == 1:
        u_2.strike()
        print('Атакует 1ый воин')
        print(
            'У воина {} осталось {} здоровья\n'.format(
                u_2.unit, u_2.health
            )
        )
    elif attacker == 2:
        u_1.strike()
        print('Атакует 2ой воин')
        print(
            'У воина {} осталось {} здоровья\n'.format(
                u_1.unit, u_1.health
            )
        )


unit_1 = Warrior(1)
unit_2 = Warrior(2)

while unit_1.health > 0 and unit_2.health > 0:
    who_attack(unit_1, unit_2)

if unit_1.health == 0:
    print('Победил воин 2')
else:
    print('Победил воин 1')
