import math


def quadraticRoots(a, b, c):
    sq = (b * b) - (4 * a * c)
    # print(math.sqrt(sq))
    if sq < 0:
        return "Imaginary"
    else:
        x = math.floor((-b + math.sqrt(sq)) / (2 * a))
        y = math.floor((-b - math.sqrt(sq)) / (2 * a))
        return x, y


print(quadraticRoots(280, 399, 573))
