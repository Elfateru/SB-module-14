import math

def radius_point(x, y, r):
    radius = math.sqrt((x*2)**2 + (y*2)**2) / 2
    if r >= radius:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))

point = radius_point(x, y, r)
