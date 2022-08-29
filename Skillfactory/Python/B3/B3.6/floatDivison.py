# Функция деления числа с плавающей точкой
def floatDivision(num, delNum, tochnost=16):
    strNum = str(num / delNum)
    if len(strNum) >= 17:
        strNum = strNum[:16]
        saver = strNum.split('.')[1]
        saver = len(saver) + 1
    else:
        saver = strNum.split('.')[1]
        saver = len(saver)

    if (tochnost < len(str(num / delNum))) or (saver == 1):
        if tochnost < 1:
            return {'full': strNum[0:strNum.index('.')], 'short': ''}
        return {'full': strNum[0:tochnost + strNum.index('.') + 1], 'short': ''}

    stranger = num % delNum

    for i in range(1, tochnost):
        stranger = stranger * 10 % delNum
        if i % (saver - 1) == 0:
            strNum += str(stranger / delNum)[2:saver + 1]

    last = strNum[strNum.index('.') + 1:tochnost + strNum.index('.') + 1]

    for index in range(tochnost):
        if last[0:index:] == last[-index::] and len(last[-index::]) > 1:
            for i in range(tochnost):
                if last[0:index + i] == last[-2 * index - i:-index]:
                    last = last[0:index + i]
                    return {'full': strNum[0:tochnost + strNum.index('.') + 1],
                            'short': strNum[0:strNum.index('.') + 1] + last + f'E-{len(last)}'}
        elif last[0:index:] == last[-index::] and len(last[-index::]) == 1:
            for i in range(1, tochnost):
                if last[0:index + i] == last[-2 * index - i:-index]:
                    last = last[0:index + i]
                    return {'full': strNum[0:tochnost + strNum.index('.') + 1],
                            'short': strNum[0:strNum.index('.') + 1] + last + f'E-{len(last)}'}

    return {'full': strNum[0:tochnost + strNum.index('.') + 1], 'short': ''}


# num = 1634564657
# num = 14657
# delNum = 23



# num = 100
# delNum = 25


num = 178
delNum = 63

tochnost = 300

div = floatDivision(num, delNum, tochnost)

print('Обычное деление -', num / delNum)
print('   Полное число -', div['full'])
print(' Краткая запись -', div['short'])
