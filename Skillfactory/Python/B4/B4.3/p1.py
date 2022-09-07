x = 3


def func():
    print(x)
    globalX = x
    globalX += 5
    return globalX


print(func())
