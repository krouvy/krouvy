def isDiv(n, a):
    if n % a == 0:
        print(f'Число {a} является делителем числа {n}')
    else:
        print(f'Число {a} не является делителем числа {n}')


isDiv(7, 6)
isDiv(8, 4)
isDiv(9, 3)
isDiv(10, 2)
isDiv(11, 1)
