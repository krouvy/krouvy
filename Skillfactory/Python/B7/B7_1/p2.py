class Square:
    def __init__(self, width):
        self.width = width

    def getArea(self):
        return self.width ** 2


class SquareFactory:

    @staticmethod
    def getWidth(width):
        return Square(width)


sq1 = SquareFactory.getWidth(17)
print(sq1.getArea())
