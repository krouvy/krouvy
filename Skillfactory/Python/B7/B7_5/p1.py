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


class GameProccess:

    def __init__(self, name='name'):
        self.playerName = name
        self.playerShips = Flot()
        self.computerShips = Flot()

    def StartPlacementShips(self):
        allShips = self.playerShips.getAllShips()

        for ship in allShips:
            tryShipPlace(self.playerShips.realField, self.playerShips.displayField, ship.size, ship.coords,
                         self.playerName)


# Функция располагает на поле корабль
def tryShipPlace(field, visionField, size, coords, name='computer'):
    print('Установка корабля')
    printField(visionField)

    while size:
        placeBoofer = []
        coord = getCoordinage()

        # Если первая точка не занята
        if field[coord[0]][coord[1]] == 'О':
            # Получение буферов возможных точек
            # для установки для разных кораблей
            if size == 3:
                placeBoofer = getBigShipBoofer(field, coord)
            elif size == 2:
                placeBoofer = getMidShipBoofer(field, coord)
            elif size == 1:
                print('Не готово')

            # Если буфер возможных точек остался пустым, то к началу цикла
            if len(placeBoofer) == 0:
                print('Нет вариантов для установки точки')
                continue
            else:
                readyBoofer = []

                # Цикл исключения из буфера занятых точек
                for i in range(0, len(placeBoofer)):
                    for j in range(0, len(placeBoofer[i])):
                        if not checkShipsOutsidePoint(placeBoofer[i][j], field):
                            placeBoofer[i][j] = False
                # Цикл заполнения нового буфера свободных точек
                for i in range(0, len(placeBoofer)):
                    if False not in placeBoofer[i]:
                        readyBoofer.append(placeBoofer[i])

                # Если новый буфер не заполнился,
                # то из этой точки не поставить корабль,
                # переход к началу цикла
                if len(readyBoofer) == 0:
                    print('Нет вариантов для установки точки')
                    continue
                else:
                    # Иначе заполняем на видимом поле первую точку
                    coords[0] = coord
                    visionField[coords[0][0]][coords[0][1]] = 'S'
                    printField(visionField)

                    # Уменьшаем стартовый размер корабля на 1
                    size -= 1

                    # цикл установки второй точки
                    while size:
                        # Новый буфер, который будет хранить совпадение
                        # уже двух точек
                        lastBoofer = []

                        secondCoord = getCoordinage()

                        # Если 2 точки присутвуют в буфере, добавляем их в новый буфер
                        for readyCoord in readyBoofer:
                            if coords[0] in readyCoord and secondCoord in readyCoord:
                                lastBoofer.append(readyCoord)

                        # Если буфер остался пустым
                        if len(lastBoofer) == 0:
                            # если это корабль длиной 2 клетки
                            if size == 1:
                                # И точка уже была введена этим кораблем
                                if secondCoord in coords:
                                    print('Координата занята')
                                else:
                                    # Проверяю есть ли эта точка в первом буфере
                                    for readyCoord in readyBoofer:
                                        if secondCoord in readyCoord:
                                            # Если да, то рисую корабль длинной 2 клетки
                                            coords[1] = secondCoord
                                            visionField[coords[1][0]][coords[1][1]] = 'S'
                                            printField(visionField)
                                            size -= 1
                                            # Заполняю реальное поле координатами корабля
                                            for finalCoord in coords:
                                                field[finalCoord[0]][finalCoord[1]] = 'S'
                                            break
                                    # если цикл корабль длинной 2 клетки не нарисовался,
                                    # то переход к началу цикла
                                    if size == 1:
                                        print('Нельзя так располагать корабль')
                                        continue
                            # если корабль в 3 клетки, но второй
                            # буфер остался пустым
                            else:
                                print('Нельзя так располагать корабль')
                                continue
                        # Если новый буфер не пустой
                        else:
                            # проверка не было ли повтора
                            if secondCoord in coords:
                                print('Координата занята')
                            # если без повтора,
                            # то устанавливается вторая координата
                            else:
                                coords[1] = secondCoord
                                visionField[coords[1][0]][coords[1][1]] = 'S'
                                printField(visionField)
                                size -= 1
                                # Если это корабль длинной 2 клетки,
                                # то заполняем реальное поле и останавливаем цикл
                                if size == 0:
                                    for finalCoord in coords:
                                        field[finalCoord[0]][finalCoord[1]] = 'S'
                                break
                    # Если цикл не был остановлен,
                    # то включается цикл подбора
                    # последней точки
                    while size:
                        lastCoord = getCoordinage()

                        for lastBooferCord in lastBoofer:
                            if lastCoord in lastBooferCord:
                                if lastCoord in coords:
                                    print('Координата занята')
                                else:
                                    coords[2] = lastCoord
                                    visionField[coords[2][0]][coords[2][1]] = 'S'
                                    printField(visionField)
                                    size = 0
                                    for finalCoord in coords:
                                        field[finalCoord[0]][finalCoord[1]] = 'S'

                        if size == 1:
                            print('Нельзя так располагать корабль', size)
        else:
            print('Точка занята')
    print('Корабль установлен')


# Функция проверяет поля вокруг точки
# если в точке есть корабль, возвращает False
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
                if field[coord[0] - 1][coord[1]] == 'О' and field[coord[0]][coord[1] - 1] == 'О':
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


# Проверяет входит ли точка в размер поля
def checkOutOfRange(coord):
    if coord >= 0 and coord <= 5:
        return True
    else:
        False


# Функция возвращает буфер возможных точек для
# Расположения корабля в 3 клетки
def getBigShipBoofer(field, coord):
    placeBoofer = []

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

    return placeBoofer


# Функция возвращает буфер возможных точек для
# Расположения корабля в 2 клетки
def getMidShipBoofer(field, coord):
    placeBoofer = []

    if checkOutOfRange(coord[1] + 1):
        if field[coord[0]][coord[1] + 1] == 'О':
            placeBoofer.append([coord, [coord[0], coord[1] + 1]])
    if checkOutOfRange(coord[1] - 1):
        if field[coord[0]][coord[1] - 1] == 'О':
            placeBoofer.append([coord, [coord[0], coord[1] - 1]])
    if checkOutOfRange(coord[0] + 1):
        if field[coord[0] + 1][coord[1]] == 'О':
            placeBoofer.append([coord, [coord[0] + 1, coord[1]]])
    if checkOutOfRange(coord[0] - 1):
        if field[coord[0] - 1][coord[1]] == 'О':
            placeBoofer.append([coord, [coord[0] - 1, coord[1]]])

    return placeBoofer


class Flot:

    def __init__(self):
        self.realField = [
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
        ]

        self.displayField = [
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
            ['О', 'О', 'О', 'О', 'О', 'О'],
        ]

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


gameProccess = GameProccess()

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
