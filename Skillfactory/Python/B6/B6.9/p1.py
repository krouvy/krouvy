# from ..B6_8.p3 import Rectangle

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getPloshad(self):
        return self.height * self.width

class Square:
    def __init__(self, width):
        self.width = width
        self.height = width

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getPloshad(self):
        return self.height ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def getLength(self):
        return 2 * 3.14 * self.radius

    def getPloshad(self):
        return self.getLength() ** 2 / 4 * 3.14

R1 = Rectangle(27, 4)
R2 = Rectangle(12, 7)

S1 = Square(35)
S2 = Square(17)

С1 = Circle(12)
С2 = Circle(19)

figures = [R1, R2, S1, S2, С1, С2]

for figure in figures:
    if isinstance(figure, Square):
        print('Квадрат', end=' ')
    elif isinstance(figure, Rectangle):
        print('Прямоугольник', end=' ')
    else:
        print('Круг', end=' ')
    print(figure.getPloshad())