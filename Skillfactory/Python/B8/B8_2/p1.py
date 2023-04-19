try:
    n = 12//0
    raise ZeroDivisionError
except ZeroDivisionError:
    print('Деление на ноль')
except ArithmeticError:
    print('Арифмитическая ошибка')
