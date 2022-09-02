def strangeFunction(args):
    print(args)
    moka = args
    count = 0
    for i in moka:
        count += i
    print(count)
    return ''


def strangeFunction2(a):
    print(a + 'a')
    return int(a)


strangeFunction(list(map(strangeFunction2, input('Введите 3 числа ').split())))
