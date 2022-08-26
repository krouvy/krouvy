num = 178
delNum = 63

numbers = [520, 160, 340, 250, 610, 430]
Minuses = []
differs = [16, 34, 25, 61, 43, 52]

listNum = []

strNum = str(num / delNum)

strNum = strNum[strNum.index('.') + 1:]

for i in strNum:
    if i in listNum:
        break
    else:
        listNum.append(i)

listNum = list(map(int, list(listNum)))

print(listNum)

for i in listNum:
    Minuses.append(i * delNum)

print(Minuses, '\n')

single = []
many = []

for i, value1 in enumerate(Minuses):
    for j, value2 in enumerate(Minuses):
        diff = value1 - value2
        if abs(diff) not in Minuses:
            single.append(diff)
        else:
            many.append(diff)
            # print('index -', Minuses.index(abs(diff)))
        # print(f'{value1} - {value2} =', diff, )

print(set(many), '\n', set(single), '\n')

single = many + single

single2 = []
many2 = []

for i, value1 in enumerate(single):
    for j, value2 in enumerate(single):
        diff = value1 - value2
        if abs(diff) not in Minuses and abs(diff) not in single:
            single2.append(diff)
        else:
            many2.append(diff)

superSet = many2 + single2

superSet = list(set(map(abs, superSet)))

print('Суперсет1 ', superSet)

for i in set(superSet):
    print(i // 63)
