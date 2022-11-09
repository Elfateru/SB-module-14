class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = [kid for kid in children if kid.age + 16 <= self.age]

    def info(self):
        print('Name: {}\nAge: {}\nChildren: {}'.format(
            self.name, self.age, ' '.join([x.name for x in self.children])
        )
        )

    def calm_kid(self, name):
        for i_kid in self.children:
            if i_kid.name == name:
                i_kid.calm = True

    def feed_kid(self, name):
        for i_kid in self.children:
            if i_kid.name == name:
                i_kid.hunger = False


class Child:

    def __init__(self, name, age, calm=False, hunger=True):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger


c_1 = Child('Petya', 9)
c_2 = Child('Masha', 8)
p = Parent('Vasya', 26, [c_1, c_2])
p.info()
p.calm_kid('Petya')
print(c_1.calm)
