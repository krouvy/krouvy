def fib():
    a, b = 0, 1
    i = 1

    yield a
    yield b

    print("То, что функция имеет в начале", a, b)

    while True:
        a, b = b, a + b
        i += 1
        # print(b, a)
        if b == 80962618193714031895056073532586929100700632223772064294846693785378138632320496195528151124350259251085346578405507826210:
            yield b
            yield i
            # return 0


for i in fib():
    print(i)

print('что она вернула в конце', *fib())
print('end')
