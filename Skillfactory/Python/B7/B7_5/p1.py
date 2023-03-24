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
                    return [coordinates[0] - 1, coordinates[1] - 1]
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
            ['О', 'О', '1', '1', 'О', '1'],
            ['О', 'О', 'О', 'О', '1', 'О'],
            ['О', 'О', 'О', '1', 'О', 'О'],
            ['О', 'О', '1', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
        ]
        self.playerShips = Flot()
        self.computerShips = Flot()
        printField(self.visField)

    def StartPlacementShips(self):
        allShips = self.playerShips.getAllShips()
        print(allShips[0].size, allShips[0].coords)

        tryShipPlace(self.realField, allShips[0].size, allShips[0].coords)

        while True:
            testField = self.realField
            for i in range(0, allShips[0].size):
                coord = getCoordinage()
                print('Координаты', coord)
                testField[coord[0]][coord[1]] = '*'
                printField(testField)


def tryShipPlace(field, size=3, coords=1):

    while size:
        placeBoofer = []
        coord = getCoordinage()
        print(coord)

        if field[coord[0]][coord[1]] == 'О':

            if size == 3:
                if checkOutOfRange(coord[1] + 1) and checkOutOfRange(coord[1] + 2):
                    if field[coord[0]][coord[1] + 1] == 'О' and field[coord[0]][coord[1] + 2] == 'О':
                        placeBoofer.append([coord, [coord[0], coord[1] + 1], [coord[0], coord[1] + 2]])
                if checkOutOfRange(coord[1] - 1) and checkOutOfRange(coord[1] - 2):
                    if field[coord[0]][coord[1] - 1] == 'О' and field[coord[0]][coord[1] - 2] == 'О':
                        placeBoofer.append([coord, [coord[0], coord[1] - 1], [coord[0], coord[1] - 2]])
                if checkOutOfRange(coord[1] - 1) and checkOutOfRange(coord[1] + 1):
                    if field[coord[0]][coord[1] - 1] == 'О' and field[coord[0]][coord[1] + 1] == 'О':
                        placeBoofer.append([coord, [coord[0], coord[1] - 1], [coord[0], coord[1] + 1]])
                if checkOutOfRange(coord[0] + 1) and checkOutOfRange(coord[0] + 2):
                    if field[coord[0] + 1][coord[1]] == 'О' and field[coord[0] + 2][coord[1]] == 'О':
                        placeBoofer.append([coord, [coord[0] + 1, coord[1]], [coord[0] + 2, coord[1]]])
                if checkOutOfRange(coord[0] - 1) and checkOutOfRange(coord[0] - 2):
                    if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0] - 2][coord[1]] == 'О':
                        placeBoofer.append([coord, [coord[0] - 1, coord[1]], [coord[0] - 2, coord[1]]])
                if checkOutOfRange(coord[0] - 1) and checkOutOfRange(coord[0] + 1):
                    if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0] + 1][coord[1]] == 'О':
                        placeBoofer.append([coord, [coord[0] - 1, coord[1]], [coord[0] + 1, coord[1]]])
            elif size == 2:
                print('Не готово')
            elif size == 1:
                print('Не готово')

            if len(placeBoofer) == 0:
                print('Нет вариантов для установки точки')
                continue
            else:
                readyBoofer = []

                for i in range(0, len(placeBoofer)):
                    for j in range(0, len(placeBoofer[i])):
                        if not checkShipsOutsidePoint(placeBoofer[i][j], field):
                            placeBoofer[i][j] = False

                for i in range(0, len(placeBoofer)):
                    if False not in placeBoofer[i]:
                        readyBoofer.append(placeBoofer[i])

                if len(readyBoofer) == 0:
                    print('Нет вариантов для установки точки')
                    continue

                print('Возможные варианты установки', readyBoofer)

                coords[0] = coord
                print(coords)
                print('Вторая координата')
                while size:
                    secondCoord= getCoordinage()

                    for readyCoord in readyBoofer:
                        if secondCoord in readyCoord:
                            coords[1] = secondCoord
                            size -= 1
                            readyBoofer = readyCoord
                            continue
                    if size == 2:
                        print('Нельзя так располагать корабль')
                        continue

                    while size:
                        print(coords)
                        lastCoord = getCoordinage()

                        if lastCoord in readyBoofer:
                            coords[2] = lastCoord
                            size -= 1

                        if size == 1:
                            print('Нельзя так располагать корабль')
                            continue
        else:
            print('Точка занята')
    print('Готово', coords)


def checkShipsOutsidePoint(coord, field):
    if all([coord[0] >= 1,
            coord[0] <= 4,
            coord[1] >= 1,
            coord[1] <= 4]):
        if all([field[coord[0] - 1][coord[1]] == 'О',
                field[coord[0] + 1][coord[1]] == 'О',
                field[coord[0]][coord[1] - 1] == 'О',
                field[coord[0]][coord[1] + 1] == 'О',
                ]):
            return True
        else:
            return False
    else:
        if coord[0] == 0:
            if coord[1] == 0:
              if field[coord[0] + 1][coord[1]] == 'О' and field[coord[0]][coord[1] + 1] == 'О':
                  return True
              else:
                  return False
            elif coord[1] == 5:
                if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0]][coord[1] + 1] == 'О':
                    return True
                else:
                    return False
            else:
                if all([field[coord[0] - 1][coord[1]] == 'О',
                        field[coord[0] + 1][coord[1]] == 'О',
                        field[coord[0]][coord[1] + 1] == 'О']):
                    return True
                else:
                    return False
        elif coord[0] == 5:
            if coord[1] == 0:
              if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0]][coord[1] + 1] == 'О':
                  return True
              else:
                  return False
            elif coord[1] == 5:
                if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0]][coord[1] - 1] == 'О':
                    return True
                else:
                    return False
            else:
                if all([field[coord[0] - 1][coord[1]] == 'О',
                        field[coord[0]][coord[1] + 1] == 'О',
                        field[coord[0]][coord[1] - 1] == 'О']):
                    return True
                else:
                    return False
        else:
            if coord[1] == 0:
                if coord[0] == 0:
                    if field[coord[0] + 1][coord[1]] == 'О' and field[coord[0]][coord[1] + 1] == 'О':
                        return True
                    else:
                        return False
                elif coord[0] == 5:
                    if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0]][coord[1] + 1] == 'О':
                        return True
                    else:
                        return False
                else:
                    if all([
                        field[coord[0] - 1][coord[1]] == 'О',
                        field[coord[0] + 1][coord[1]] == 'О',
                        field[coord[0]][coord[1] + 1] == 'О'
                    ]):
                        return True
                    else:
                        return False
            elif coord[1] == 5:
                if coord[0] == 0:
                    if field[coord[0] + 1][coord[1]] == 'О' and field[coord[0]][coord[1] - 1] == 'О':
                        return True
                    else:
                        return False
                elif coord[0] == 5:
                    if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0]][coord[1] - 1] == 'О':
                        return True
                    else:
                        return False
                else:
                    if all([field[coord[0] - 1][coord[1]] == 'О',
                            field[coord[0] + 1][coord[1]] == 'О',
                            field[coord[0]][coord[1] - 1] == 'О']):
                        return True
                    else:
                        return False

def checkOutOfRange(coord):
    if coord >= 0 and coord <= 5:
        return True
    else:
        False


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
