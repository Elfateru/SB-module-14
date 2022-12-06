from math import cos, sin, radians

class Car:
    def __init__(self, x=0, y=0, angle=0):
        self.__x = x
        self.__y = y
        self.__angle = angle

    def __str__(self):
        return 'X: {}\nY: {}\nDirection: {}\n'.format(
            self.__x, self.__y, self.__angle
        )

    def move(self, distance):
        angle = radians(self.__angle)
        self.__x = round(self.__x + distance * (cos(angle)), 2)
        self.__y = round(self.__y + distance * (sin(angle)), 2)

    def turn(self, angle):
        self.__angle = angle

class Bus(Car):
    def __init__(self):
        super().__init__()
        self.__passengers = 0
        self._money = 0

    def move(self, distance):
        super().move(distance)
        self._money += self.__passengers * (distance // 100)

    def turn(self, angle):
        super().turn(angle)

    def enter(self, passenger):
        self.__passengers += passenger

    def exit(self, passenger):
        if self.__passengers >= passenger:
            self.__passengers -= passenger
        else:
            self.__passengers = 0
