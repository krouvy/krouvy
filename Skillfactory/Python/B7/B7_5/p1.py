import random

shipHitted = '□'
shipSimbol = '■'
clearSimbol = ' '
bombSimbol = '●'
fieldSize = 5


def getRandomCoordinate():
    return [random.randint(0, fieldSize - 1), random.randint(0, fieldSize - 1)]


def getRandomBoofer(booferLen):
    return random.randint(0, booferLen)


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
                    coordinates[0] <= fieldSize,
                    coordinates[1] >= 1,
                    coordinates[1] <= fieldSize
                ]):
                    return [coordinates[0] - 1, coordinates[1] - 1]
                else:
                    print('Введены неверные координаты')
            else:
                print('Несоответвующее количество координат')
        except ValueError:
            print('Координаты должны состоять только из цифр')


# Функция располагает на поле корабль
def tryShipPlace(field, visionField, size, coords, name='computer'):
    countTryPlacement = 0

    if not name == 'computer':
        print('Установка корабля')
        printField(visionField)

    while size and countTryPlacement <= 70:
        countTryPlacement += 1
        placeBoofer = []
        if name == 'computer':
            coord = getRandomCoordinate()
        else:
            coord = getCoordinage()

        # Если первая точка не занята
        if field[coord[0]][coord[1]] == clearSimbol:
            # Получение буферов возможных точек
            # для установки для разных кораблей
            if size == 3:
                placeBoofer = getBigShipBoofer(field, coord)
            elif size == 2:
                placeBoofer = getMidShipBoofer(visionField, coord)
            elif size == 1:
                if name == 'computer':
                    if checkLitShip(field, coord):
                        field[coord[0]][coord[1]] = shipSimbol
                        break
                    else:
                        continue
                else:
                    if checkLitShip(visionField, coord):
                        coords[0] = coord
                        visionField[coords[0][0]][coords[0][1]] = shipSimbol
                        field[coords[0][0]][coords[0][1]] = shipSimbol
                        printField(visionField)
                        break
                    else:
                        if not name == 'computer':
                            print('В эту точку нельзя ставить корабль')
                        continue

            # Если буфер возможных точек остался пустым, то к началу цикла
            if len(placeBoofer) == 0:
                if not name == 'computer':
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
                    if not name == 'computer':
                        print('Нет вариантов для установки точки')
                    continue
                else:
                    # Иначе заполняем на видимом поле первую точку
                    coords[0] = coord
                    if not name == 'computer':
                        visionField[coords[0][0]][coords[0][1]] = shipSimbol
                        printField(visionField)

                    # Уменьшаем стартовый размер корабля на 1
                    size -= 1

                    # цикл установки второй точки
                    while size and countTryPlacement <= 70:
                        # Новый буфер, который будет хранить совпадение
                        # уже двух точек
                        lastBoofer = []
                        countTryPlacement += 1

                        if name == 'computer':
                            getRand = getRandomBoofer(len(readyBoofer) - 1)
                            randBoofer = readyBoofer[getRand]
                            for randCoord in randBoofer:
                                field[randCoord[0]][randCoord[1]] = shipSimbol
                            size = 0
                            break
                        else:
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
                                    if not name == 'computer':
                                        print('Координата занята')
                                else:
                                    # Проверяю есть ли эта точка в первом буфере
                                    for readyCoord in readyBoofer:
                                        if secondCoord in readyCoord:
                                            # Если да, то рисую корабль длинной 2 клетки
                                            coords[1] = secondCoord
                                            visionField[coords[1][0]][coords[1][1]] = shipSimbol
                                            printField(visionField)
                                            size -= 1
                                            # Заполняю реальное поле координатами корабля
                                            for finalCoord in coords:
                                                field[finalCoord[0]][finalCoord[1]] = shipSimbol
                                            break
                                    # если цикл корабль длинной 2 клетки не нарисовался,
                                    # то переход к началу цикла
                                    if size == 1:
                                        if not name == 'computer':
                                            print('Нельзя так располагать корабль')
                                        continue
                            # если корабль в 3 клетки, но второй
                            # буфер остался пустым
                            else:
                                if not name == 'computer':
                                    print('Нельзя так располагать корабль')
                                continue
                        # Если новый буфер не пустой
                        else:
                            # проверка не было ли повтора
                            if secondCoord in coords:
                                if not name == 'computer':
                                    print('Координата занята')
                            # если без повтора,
                            # то устанавливается вторая координата
                            else:
                                coords[1] = secondCoord
                                visionField[coords[1][0]][coords[1][1]] = shipSimbol
                                printField(visionField)
                                size -= 1
                                # Если это корабль длинной 2 клетки,
                                # то заполняем реальное поле и останавливаем цикл
                                if size == 0:
                                    for finalCoord in coords:
                                        field[finalCoord[0]][finalCoord[1]] = shipSimbol
                                break
                    # Если цикл не был остановлен,
                    # то включается цикл подбора
                    # последней точки
                    while size and countTryPlacement <= 70:
                        countTryPlacement += 1
                        lastCoord = getCoordinage()

                        for lastBooferCord in lastBoofer:
                            if lastCoord in lastBooferCord:
                                if lastCoord in coords:
                                    if not name == 'computer':
                                        print('Координата занята')
                                else:
                                    coords[2] = lastCoord
                                    visionField[coords[2][0]][coords[2][1]] = shipSimbol
                                    printField(visionField)
                                    size = 0
                                    for finalCoord in coords:
                                        field[finalCoord[0]][finalCoord[1]] = shipSimbol

                        if size == 1:
                            if not name == 'computer':
                                print('Нельзя так располагать корабль', size)
        else:
            if not name == 'computer':
                print('Точка занята')
    if not name == 'computer':
        print('Корабль установлен')
    if countTryPlacement >= 70:
        print('Не удалось установить корабль')
        return False
    else:
        return True


# Функция проверяет поля вокруг точки
# если в точке есть корабль, возвращает False
def checkShipsOutsidePoint(coord, field):
    if all([coord[0] >= 1,
            coord[0] <= fieldSize - 2,
            coord[1] >= 1,
            coord[1] <= fieldSize - 2]):
        if all([field[coord[0] - 1][coord[1]] == clearSimbol,
                field[coord[0] + 1][coord[1]] == clearSimbol,
                field[coord[0]][coord[1] - 1] == clearSimbol,
                field[coord[0]][coord[1] + 1] == clearSimbol,
                ]):
            return True
        else:
            return False
    else:
        if coord[0] == 0:
            if coord[1] == 0:
                if field[coord[0] + 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] + 1] == clearSimbol:
                    return True
                else:
                    return False
            elif coord[1] == fieldSize - 1:
                if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] - 1] == clearSimbol:
                    return True
                else:
                    return False
            else:
                if all([field[coord[0]][coord[1] - 1] == clearSimbol,
                        field[coord[0]][coord[1] + 1] == clearSimbol,
                        field[coord[0] + 1][coord[1]] == clearSimbol]):
                    return True
                else:
                    return False
        elif coord[0] == fieldSize - 1:
            if coord[1] == 0:
                if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] + 1] == clearSimbol:
                    return True
                else:
                    return False
            elif coord[1] == fieldSize - 1:
                if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] - 1] == clearSimbol:
                    return True
                else:
                    return False
            else:
                if all([field[coord[0] - 1][coord[1]] == clearSimbol,
                        field[coord[0]][coord[1] + 1] == clearSimbol,
                        field[coord[0]][coord[1] - 1] == clearSimbol]):
                    return True
                else:
                    return False
        else:
            if coord[1] == 0:
                if coord[0] == 0:
                    if field[coord[0] + 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] + 1] == clearSimbol:
                        return True
                    else:
                        return False
                elif coord[0] == fieldSize - 1:
                    if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] + 1] == clearSimbol:
                        return True
                    else:
                        return False
                else:
                    if all([
                        field[coord[0] - 1][coord[1]] == clearSimbol,
                        field[coord[0] + 1][coord[1]] == clearSimbol,
                        field[coord[0]][coord[1] + 1] == clearSimbol
                    ]):
                        return True
                    else:
                        return False
            elif coord[1] == fieldSize - 1:
                if coord[0] == 0:
                    if field[coord[0] + 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] - 1] == clearSimbol:
                        return True
                    else:
                        return False
                elif coord[0] == fieldSize - 1:
                    if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0]][coord[1] - 1] == clearSimbol:
                        return True
                    else:
                        return False
                else:
                    if all([field[coord[0] - 1][coord[1]] == clearSimbol,
                            field[coord[0] + 1][coord[1]] == clearSimbol,
                            field[coord[0]][coord[1] - 1] == clearSimbol]):
                        return True
                    else:
                        return False


# Проверяет входит ли точка в размер поля
def checkOutOfRange(coord):
    if coord >= 0 and coord <= fieldSize - 1:
        return True
    else:
        False


# Функция возвращает буфер возможных точек для
# Расположения корабля в 3 клетки
def getBigShipBoofer(field, coord):
    placeBoofer = []

    if checkOutOfRange(coord[1] + 1) and checkOutOfRange(coord[1] + 2):
        if field[coord[0]][coord[1] + 1] == clearSimbol and field[coord[0]][coord[1] + 2] == clearSimbol:
            placeBoofer.append([coord, [coord[0], coord[1] + 1], [coord[0], coord[1] + 2]])
    if checkOutOfRange(coord[1] - 1) and checkOutOfRange(coord[1] - 2):
        if field[coord[0]][coord[1] - 1] == clearSimbol and field[coord[0]][coord[1] - 2] == clearSimbol:
            placeBoofer.append([coord, [coord[0], coord[1] - 1], [coord[0], coord[1] - 2]])
    if checkOutOfRange(coord[1] - 1) and checkOutOfRange(coord[1] + 1):
        if field[coord[0]][coord[1] - 1] == clearSimbol and field[coord[0]][coord[1] + 1] == clearSimbol:
            placeBoofer.append([coord, [coord[0], coord[1] - 1], [coord[0], coord[1] + 1]])
    if checkOutOfRange(coord[0] + 1) and checkOutOfRange(coord[0] + 2):
        if field[coord[0] + 1][coord[1]] == clearSimbol and field[coord[0] + 2][coord[1]] == clearSimbol:
            placeBoofer.append([coord, [coord[0] + 1, coord[1]], [coord[0] + 2, coord[1]]])
    if checkOutOfRange(coord[0] - 1) and checkOutOfRange(coord[0] - 2):
        if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0] - 2][coord[1]] == clearSimbol:
            placeBoofer.append([coord, [coord[0] - 1, coord[1]], [coord[0] - 2, coord[1]]])
    if checkOutOfRange(coord[0] - 1) and checkOutOfRange(coord[0] + 1):
        if field[coord[0] - 1][coord[1]] == clearSimbol and field[coord[0] + 1][coord[1]] == clearSimbol:
            placeBoofer.append([coord, [coord[0] - 1, coord[1]], [coord[0] + 1, coord[1]]])

    return placeBoofer


# Функция возвращает буфер возможных точек для
# Расположения корабля в 2 клетки
def getMidShipBoofer(field, coord):
    placeBoofer = []

    if checkOutOfRange(coord[1] + 1):
        if field[coord[0]][coord[1] + 1] == clearSimbol:
            placeBoofer.append([coord, [coord[0], coord[1] + 1]])
    if checkOutOfRange(coord[1] - 1):
        if field[coord[0]][coord[1] - 1] == clearSimbol:
            placeBoofer.append([coord, [coord[0], coord[1] - 1]])
    if checkOutOfRange(coord[0] + 1):
        if field[coord[0] + 1][coord[1]] == clearSimbol:
            placeBoofer.append([coord, [coord[0] + 1, coord[1]]])
    if checkOutOfRange(coord[0] - 1):
        if field[coord[0] - 1][coord[1]] == clearSimbol:
            placeBoofer.append([coord, [coord[0] - 1, coord[1]]])

    return placeBoofer


def checkLitShip(field, coord):
    placeBoofer = []

    if checkOutOfRange(coord[1] + 1):
        if field[coord[0]][coord[1] + 1] == clearSimbol:
            placeBoofer.append(True)
        else:
            placeBoofer.append(False)
    if checkOutOfRange(coord[1] - 1):
        if field[coord[0]][coord[1] - 1] == clearSimbol:
            placeBoofer.append(True)
        else:
            placeBoofer.append(False)
    if checkOutOfRange(coord[0] + 1):
        if field[coord[0] + 1][coord[1]] == clearSimbol:
            placeBoofer.append(True)
        else:
            placeBoofer.append(False)
    if checkOutOfRange(coord[0] - 1):
        if field[coord[0] - 1][coord[1]] == clearSimbol:
            placeBoofer.append(True)
        else:
            placeBoofer.append(False)

    if False in placeBoofer:
        return False
    else:
        return True


def shoot(coord, flotSize, displayField, realField):
    if not displayField[coord[0]][coord[1]] == bombSimbol and not displayField[coord[0]][coord[1]] == shipHitted:
        if realField[coord[0]][coord[1]] == shipSimbol:
            print('Попадание')
            realField[coord[0]][coord[1]] = shipHitted
            displayField[coord[0]][coord[1]] = shipHitted
            flotSize -= 1
            print('Оставшийся флот', flotSize)
            return [False, flotSize]
        else:
            print('Мимо')
            displayField[coord[0]][coord[1]] = bombSimbol
            print('Оставшийся флот', flotSize)
            return [True, flotSize]
    else:
        print('В эту точку уже стреляли')
    return [False, flotSize]


class GameProccess:

    def __init__(self, name='name'):
        self.playerName = name
        self.playerShips = Flot()
        self.computerShips = Flot()

    def startPlacementShips(self):

        playerShips = self.playerShips.getAllShips()
        computerShips = self.computerShips.getAllShips()

        error = 0

        while error <= 3:
            for ship in computerShips:
                shipPlacement = tryShipPlace(self.computerShips.realField, self.computerShips.displayField, ship.size,
                                             ship.coords)
                if shipPlacement:
                    continue
                else:
                    error += 1
                    self.computerShips.realField = [[clearSimbol for _ in range(0, fieldSize)] for _ in
                                                    range(0, fieldSize)]
                    self.computerShips.displayField = [[clearSimbol for _ in range(0, fieldSize)] for _ in
                                                       range(0, fieldSize)]
                    print('Ошибка, корабли требуется установить заново')
                    break
            if error == 0:
                break

        if error >= 3:
            print('Программе не удалось установить корабли для соперника, попробуйте увеличить размер поля')
            return False

        for ship in playerShips:
            tryShipPlace(self.playerShips.realField, self.playerShips.displayField, ship.size,
                         ship.coords, self.playerName)

    def startFight(self):

        computerFlotSize = self.computerShips.flotSize
        playerFlotSize = self.playerShips.flotSize

        computerShoot = False
        arrayRandomShoot = [i for i in range(0, fieldSize ** 2)]

        while computerFlotSize > 0 and playerFlotSize > 0:

            if computerShoot:
                print('Ходит компьютер...')

                randShoot = arrayRandomShoot.pop(random.randint(0, len(arrayRandomShoot) - 1))
                coord = [randShoot // fieldSize, randShoot % fieldSize]
                Shoot = shoot(coord, playerFlotSize, self.playerShips.displayField, self.playerShips.realField)
                playerFlotSize = Shoot[1]
                print('     __Ваше поле__')
                printField(self.playerShips.displayField)
            else:
                print('Ходит игрок..')
                print('   __Поле компьютера__')
                printField(self.computerShips.displayField)

                coord = getCoordinage()
                Shoot = shoot(coord, computerFlotSize, self.computerShips.displayField, self.computerShips.realField)
                computerFlotSize = Shoot[1]
                if Shoot[0]:
                    print('   __Поле компьютера__')
                    printField(self.computerShips.displayField)

            if Shoot[0]:
                computerShoot = not computerShoot

        if computerFlotSize == 0:
            print('Победил игрок')
            print('   __Поле компьютера__')
            printField(self.computerShips.displayField)
        else:
            print('Победил компьютер')
            print('     __Ваше поле__')
            printField(self.playerShips.displayField)


class Flot:

    def __init__(self):
        self.realField = [[clearSimbol for _ in range(0, fieldSize)] for _ in range(0, fieldSize)]
        self.displayField = [[clearSimbol for _ in range(0, fieldSize)] for _ in range(0, fieldSize)]

        self.bigShip = Ship(3)
        self.midShip1 = Ship(2)
        self.midShip2 = Ship(2)
        self.litShip1 = Ship(1)
        self.litShip2 = Ship(1)
        self.litShip3 = Ship(1)

        self.flotSize = 10
        # self.flotSize = self.getFlotSize()

    def getAllShips(self):
        return [self.bigShip, self.midShip1, self.midShip2, self.litShip1, self.litShip2, self.litShip3]

    def getFlotSize(self):
        Ships = self.getAllShips()
        size = 0
        for Ship in Ships:
            size += Ship.size
        return size


class Ship:

    def __init__(self, size):
        self.size = size
        self.coords = [[None, None] for _ in range(0, size)]


gameProccess = GameProccess()
gameProccess.startPlacementShips()
gameProccess.startFight()
