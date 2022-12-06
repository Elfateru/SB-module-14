# class Person:
#     def __init__(self, name, surname, age):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age
#
#     def __str__(self):
#         return 'Работник: {} {}\nВозраст: {}\nПрофессия: {}\nЗапрлата: {}'.format(
#             self.__surname, self.__name, self.__age, self.__class__.__name__, self.__class__.salary(self)
#         )
#
#
#
# class Employee(Person):
#
#     def salary(self):
#         pass
#
#
# class Manager(Employee):
#
#     def salary(self):
#         return 13000
#
#
# class Agent(Employee):
#
#     def __init__(self, name, surname, age, sales):
#         super().__init__(name, surname, age)
#         self.__sales = sales
#
#     def salary(self):
#         return 5000 + (self.__sales * 0.05)
#
#
# class Worker(Employee):
#
#     def __init__(self, name, surname, age, w_hours):
#         super().__init__(name, surname, age)
#         self.__w_hours = w_hours
#
#     def salary(self):
#         return 100 * self.__w_hours
#
#
# m_1 = Manager('Vasya', 'Vasin', 35)
# m_2 = Manager('Petya', 'Vasin', 28)
# m_3 = Manager('Jenya', 'Vasin', 32)
# a_1 = Agent('Vasya', 'Petin', 45, 10000)
# a_2 = Agent('Petya', 'Petin', 24, 20000)
# a_3 = Agent('Jenya', 'Petin', 35, 30000)
# w_1 = Worker('Vasya', 'Jenin', 24, 40)
# w_2 = Worker('Petya', 'Jenin', 25, 80)
# w_3 = Worker('Jenya', 'Jenin', 26, 120)
#
# workers_list = [m_1, m_2, m_3, a_1, a_2, a_3, w_1, w_2, w_3]
#
# for employee in workers_list:
#     print(employee, '\n')
class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def __str__(self):
        return 'Работник: {} {}\nВозраст: {}\nПрофессия: {}\nЗапрлата: {}'.format(
            self.get_surname(), self.get_name(), self.get_age(), self.__class__.__name__, self.__class__.salary(self)
        )

    def salary(self):
        pass


class Manager(Employee):

    def salary(self):
        return 13000


class Agent(Employee):

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def salary(self):
        return 5000 + (self.__sales * 0.05)


class Worker(Employee):

    def __init__(self, name, surname, age, w_hours):
        super().__init__(name, surname, age)
        self.__w_hours = w_hours

    def salary(self):
        return 100 * self.__w_hours


m_1 = Manager('Vasya', 'Vasin', 35)
m_2 = Manager('Petya', 'Vasin', 28)
m_3 = Manager('Jenya', 'Vasin', 32)
a_1 = Agent('Vasya', 'Petin', 45, 10000)
a_2 = Agent('Petya', 'Petin', 24, 20000)
a_3 = Agent('Jenya', 'Petin', 35, 30000)
w_1 = Worker('Vasya', 'Jenin', 24, 40)
w_2 = Worker('Petya', 'Jenin', 25, 80)
w_3 = Worker('Jenya', 'Jenin', 26, 120)

workers_list = [m_1, m_2, m_3, a_1, a_2, a_3, w_1, w_2, w_3]

for employee in workers_list:
    print(employee, '\n')
