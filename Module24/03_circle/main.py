import math


class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.radius * math.pi

    def increase(self, k):
        self.radius *= k

    def intersection(self, comparable):
        d = math.sqrt(abs(self.x - comparable.x) ** 2 + abs(self.y - comparable.y) ** 2)
        if (self.radius + comparable.radius) >= d:
            print('Круги пересекаются')
        else:
            print('Круги не пересекаются')
