import os

file = os.listdir()[0]

file = open(file, 'r', encoding='utf8')
inFile = file.read()

for symbs in inFile:
    if symbs == '\n':
        print(' ', sep='', end='')
        continue
    print(symbs, end='')
