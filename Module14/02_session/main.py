print("Введите первую точку")

x1 = float(input('X: '))
y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2


if x_diff == 0 and y_diff == 0:
    print('Вы ввели одинаковые координаты для двух точек. Невозможно провести прямую через одну точку.')
elif x_diff == 0:
    x = x1
    print("Уравнение прямой, проходящей через эти точки:")
    print('x = ', x)
elif y_diff == 0:
    y = y1
    print("Уравнение прямой, проходящей через эти точки:")
    print('y = ', y)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)