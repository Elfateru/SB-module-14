import random


class Student:

    def __init__(self, name, group, rating):
        self.surname_name = name
        self.group = group
        self.rating = rating
        self.gpa = sum(self.rating) / 5

    def info(self):
        print('Name: {}\nGroup: {}\nRating: {}\nGPA: {}'.format(
            self.surname_name, self.group, self.rating, self.gpa))


def new_rating():
    new_list = []
    for _ in range(5):
        new_list.append(random.randint(1, 5))
    return new_list


s_1 = Student('A b', 1, new_rating())
s_2 = Student('B c', 1, new_rating())
s_3 = Student('C d', 1, new_rating())
s_4 = Student('D e', 1, new_rating())
s_5 = Student('E f', 1, new_rating())
s_6 = Student('F g', 1, new_rating())
s_7 = Student('G h', 1, new_rating())
s_8 = Student('H i', 1, new_rating())
s_9 = Student('I j', 1, new_rating())
s_10 = Student('J k', 1, new_rating())

group_list = [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]

sorted_group = sorted(group_list, key=lambda x: x.gpa)
for i in sorted_group:
    i.info()
