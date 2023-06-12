import math

def square(side):
    funk_1 = side * side
    if not isinstance(funk_1, int):
        funk_1 = math.ceil(funk_1)
    return funk_1

side = 7.8
funk_1 = square(side)
print("площадь квадрата: "  + str(side) + " равна " + str(funk_1))