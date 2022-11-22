def hodFunc(field, trigger):
    if trigger:
        symb = 'x'
    else:
        symb = '0'
    hod = list(map(int, input('Выберете координаты ').split()))
    if all([0 <= hod[0] <= 2,
            0 <= hod[1] <= 2,
            ]):
        if field[hod[0]][hod[1]] == '-':
            field[hod[0]][hod[1]] = symb
            print(*field[0], sep=' ')
            print(*field[1], sep=' ')
            print(*field[2], sep=' ')
            return not trigger
        else:
            print('Необходимы другие координаты')
    else:
        print('Необходимы другие координаты')
    return trigger


def checkWin(field):
    if any([
        field[0][0] == field[0][1] == field[0][2] == 'x',
        field[1][0] == field[1][1] == field[1][2] == 'x',
        field[2][0] == field[2][1] == field[2][2] == 'x',
        field[0][0] == field[1][1] == field[2][2] == 'x',
        field[2][0] == field[1][1] == field[0][2] == 'x',
    ]):
        print('Победа крестиков')
        return False
    elif any([
        field[0][0] == field[0][1] == field[0][2] == '0',
        field[1][0] == field[1][1] == field[1][2] == '0',
        field[2][0] == field[2][1] == field[2][2] == '0',
        field[0][0] == field[1][1] == field[2][2] == '0',
        field[2][0] == field[1][1] == field[0][2] == '0',
    ]):
        print('Победа ноликов')
        return False
    else:
        return True


field = [['-' for i in range(3)] for j in range(3)]
trigger = True
game = True

while game:
    if any([
        field[0].count('-') > 0,
        field[1].count('-') > 0,
        field[2].count('-') > 0]
    ):
        trigger = hodFunc(field, trigger)
        game = checkWin(field)
    else:
        print('Ничья')
        game = False
