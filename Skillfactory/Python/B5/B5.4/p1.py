def discrimenant(a, b, c):
    D = b ** 2 - 4 * a * c
    return D


def FindCorni(D, a, b):
    if D < 0:
        print('Нет корней')
    elif D == 0:
        print(-b / (2 * a))
    else:
        print((-b - D ** 0.5) / (2 * a))
        print((-b + D ** 0.5) / (2 * a))


def startMath(a, b, c):
    D = discrimenant(a, b, c)
    FindCorni(D, a, b)


startMath(12, 5, 0)
