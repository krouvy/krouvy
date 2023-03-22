def printField(field):
    print(' ', end=" ")
    for i in range(0, len(field)):
        print("|_", i + 1, '_', sep='', end="")
    print('|')

    for i in range(0, len(field)):
        print(i + 1, end=" ")
        for point in field[i]:
            print("|", point, end=" ")
        print('|')


def getCoordinage():
    while True:
        try:
            coordinates = list(map(int, input('Введите через пробел 2 координаты ').split()))
            if len(coordinates) == 2:
                if all([
                    coordinates[0] >= 1,
                    coordinates[0] <= 6,
                    coordinates[1] >= 1,
                    coordinates[1] <= 6
                ]):
                    return coordinates
                else:
                    print('Введены неверные координаты')
            else:
                print('Несоответвующее количество координат')
        except ValueError:
            print('Координаты должны состоять только из цифр')


class GameField:

    def __init__(self):
        self.visField = [
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
        ]
        self.realField = [
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
        ]
        self.playerShips = Flot()
        self.computerShips = Flot()
        printField(self.visField)

    def StartPlacementShips(self):
        allShips = self.playerShips.getAllShips()
        print(allShips[0].size, allShips[0].coords)
        while True:
            testField = self.realField
            for i in range(0, allShips[0].size):
                coord = getCoordinage()
                print('Координаты', coord)
                testField[coord[0]][coord[1]] = '*'
                printField(testField)


class Flot:

    def __init__(self):
        self.bigShip = Ship(3)
        self.midShip1 = Ship(2)
        self.midShip2 = Ship(2)
        self.litShip1 = Ship(1)
        self.litShip2 = Ship(1)
        self.litShip3 = Ship(1)

    def getAllShips(self):
        return [self.bigShip, self.midShip1, self.midShip2, self.litShip1, self.litShip2, self.litShip3]


class Ship:

    def __init__(self, size):
        self.size = size
        self.coords = [[None, None] for _ in range(0, size)]


gameProccess = GameField()

gameProccess.StartPlacementShips()

# playerShips = gameProccess.playerShips.getAllShips()
# for ship in playerShips:
#     print(ship.size)
#     print(ship.coords)

# field = [['О', 'О', 'О', 'О', 'О', 'О'],
#          ['О', 'О', 'О', 'О', 'О', 'О'],
#          ['О', 'О', 'О', 'О', 'О', 'О'],
#          ['О', 'О', 'О', 'О', 'О', 'О'],
#          ['О', 'О', 'О', 'О', 'О', 'О'],
#          ['О', 'О', 'О', 'О', 'О', 'О'],
#          ]
# for _ in range(1, 10):
#     printField(field)
#     coordinate = getCoordinage()
#     field[coordinate[0] - 1][coordinate[1] - 1] = '*'
