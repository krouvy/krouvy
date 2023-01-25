_MangledGlobal__mangled = 111


class MangledGlobal:
    def __init__(self):
        self.__mangled = 888
        self.__hera = 10

    def test(self):
        # Эта строка не будет работать без глобальной переменной
        a = __mangled + 89
        print('Глобальная переменная + 89 = ', a)


ora = MangledGlobal()
print(dir(ora))

print('Переменная созданная в классе ', ora._MangledGlobal__mangled)
print('Переменная созданная в классе ', ora._MangledGlobal__hera)
print('Глобальная переменная', _MangledGlobal__mangled)
ora.test()

