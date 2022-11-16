def check(a):
    if 100 <= a <= 999:
        if a % 2 == 0 and a % 3 == 0:
            print(a)


a = int(input('Введити число... '))
check(a)

for i in range(0, 1000):
    check(i)
