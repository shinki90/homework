import math

def square(side):
    funk_1 = side * side
    if not isinstance(funk_1, int):
        funk_1 = math.ceil(funk_1)
    return funk_1

side = int(input('Сторона квадрата: '))
funk_2 = square(side)
print("площадь квадрата: "  + str(side) + " равна " + str(funk_2))