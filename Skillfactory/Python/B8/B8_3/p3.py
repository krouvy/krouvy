import inspect


def numsAdd(a: int = 7, b: int = 3) -> str:
    print('Эта функция возвращает тип', globals()[inspect.stack()[0][3]].__annotations__['return'])
    """
    Стрелочная функция сложения,
    но в теории возвращающая строку
    """
    return str(a + b)


n1 = numsAdd(5, 4)
print(n1, type(n1))

n2 = numsAdd()
print(n2, type(n2))
