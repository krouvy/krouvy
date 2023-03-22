class Square:

    def __init__(self, width):
        self.__width = width

    def get_area(self):
        return self.__width ** 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print('Ширина не может быть меньше нуля')


S1 = Square(14)
print(S1.get_area())
S1.width = -12
print(S1.width)
print(S1.get_area())