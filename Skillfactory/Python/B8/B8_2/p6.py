class NonPositiveDigitException(ValueError):
    def __init__(self):
        print(self.__class__.__name__)
        super().__init__('Этот тип числа не может быть отрицательным')


class Square():
    def __init__(self, width):
            if width <= 0:
                raise NonPositiveDigitException()
            else:
                self.width = width
                print('Квадрат со сторонной', self.width)



try:
    S1 = Square(-4)
    A = 17/0
except Exception as error:
    print(error)
