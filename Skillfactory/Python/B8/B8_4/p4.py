import os

path = os.listdir()[0]

file = open(path, 'r', encoding='utf8')
inFile = file.read()
listStrings = inFile.split('\n')
stringNumber = len(listStrings)
file.close()

file = open(path, 'a', encoding='utf8')
file.write(f'\nНовая строка номер {stringNumber+1}')
file.close()


file = open(path, 'r', encoding='utf8')
inFile = file.read()

print(f'Файл содержал {stringNumber} строк\n')
print(inFile)

file.close()