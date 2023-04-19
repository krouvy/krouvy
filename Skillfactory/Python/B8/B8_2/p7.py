class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указана сторона квадрата')
        else:
            print(a)

Square(-17)