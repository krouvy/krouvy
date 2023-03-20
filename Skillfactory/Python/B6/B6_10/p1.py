class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getThisClassData(self):
        className = self.__class__.__name__
        return f'{className}({self.x},{self.y},{self.width},{self.height})'


class Square(Rectangle):
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = width


Hey = Rectangle(5, 4, 10, 20)
print(Hey.getThisClassData())

Hey2 = Square(8, 1, 17)
print(Hey2.getThisClassData())
