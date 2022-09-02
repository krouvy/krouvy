def strangeFunction(a, b, c):
    print(a + b + c)
    return ''


def strangeFunction2(a):
    print(a + 'a')
    return int(a)

strangeFunction(*list(map(strangeFunction2, input('Введите 3 числа ').split())))
