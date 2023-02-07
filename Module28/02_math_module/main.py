import math


class MyMath:

    @staticmethod
    def circle_len(radius: int or float) -> float:
        return math.pi * 2 * radius

    @staticmethod
    def circle_sq(radius: int or float) -> float:
        return math.pi * radius ** 2

    @staticmethod
    def sphere_sq(radius: int or float) -> float:
        return math.pi * 4 * radius ** 2

    @staticmethod
    def cube_vol(length: int or float) -> float:
        return length ** 3


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.sphere_sq(radius=5)
res_4 = MyMath.cube_vol(length=2.5)
print(res_1)
print(res_2)
print(res_3)
print(res_4)