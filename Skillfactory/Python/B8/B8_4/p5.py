import os

path = os.listdir()[0]

file = open(path, 'r', encoding='utf8')
inFile = file.read()

listStrings = inFile.split('\n')
stringNumber = len(listStrings)
print(f'Файл до записи\n{inFile}\n________________\n')

stopPoint = 0
strPoint = int(input('Введите номер строки для записи '))
stringToWrite = input('Введите строку, которую хотите добавить... ')

for i, item in enumerate(inFile):
    if item == '\n':
        stopPoint += 1
    if stopPoint == strPoint:
        stopPoint = i
        break

print(f'Строка для записи -  {strPoint} Точка - {stopPoint}')
print(f'Сейчас в файле {stringNumber} строк\n')

file.close()

file = open(path, 'w', encoding='utf8')
file.write(f'{inFile[0:stopPoint]} {stringToWrite} {inFile[stopPoint:]}')
file.close()
file = open(path, 'r', encoding='utf8')
print('Файл после записи\n', file.read())
