with open('input', 'r', encoding='utf8') as inputFile:
    numList = [int(i) for i in inputFile.readlines()]
    summa = max(numList) + min(numList)
    print(f"{max(numList)} + {min(numList)} = {summa}")
    print(numList)
    with open('output', 'w', encoding='utf8') as outputFile:
        outputFile.write(str(summa))
        print('Запись прошла')
