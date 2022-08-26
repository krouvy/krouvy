# num = int(input('Введите делимое '))
# delNum = int(input('Введите делитель '))
# tochnost = int(input('Введите точность '))

num = 14657
delNum = 23
tochnost = 1000

strNum = str(num / delNum)[:-1]

stranger = num % delNum

for i in range(1, tochnost):
    stranger = stranger * 10 % delNum
    if i % 12 == 0:
        strNum += str(stranger / delNum)[2:14]

print('\n' + strNum + '\n', sep='')

last = strNum[strNum.index('.') + 1:]
breaker = len(last)

reading = {}

while True:
    prom = last[:breaker]
    # print(last.count(prom), len(prom), prom)
    reading[len(prom)] = prom

    breaker //= 2
    if breaker == 1:
        break

reading = list(map(list, reading.items()))

full = None

for i in range(len(reading) - 1, -1, -1):
    # print(i, reading[i])
    state = []
    for j in range(len(reading) - 1, -1, -1):
        if j == 8 and reading[j - 1][1].count(reading[i][1]) == 0:
            full = reading[i - 1][1]
            break
        # print(reading[j - 1][1].count(reading[i][1]), end=' ')
    if full:
        break
    # print()

index = 0

while index < 30:
    # print(full[-index::])
    # print(full[0:index:])
    if full[-index::] == full[0:index:]:
        full = full[0:-index]
        break
    index += 1

print(f'Повторяющаяся последовательность {full},\nДлина - {len(full)}')
