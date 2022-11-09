def saveToDict(fn):
    def wrapper(*args, **kwargs):
        print('Начало записи')
        result = fn(*args, **kwargs)
        myDict[result[1]] = result[0]
        print('Конец записи\n')

    return wrapper


def multiply(n1, n2, index=0):
    result = n1 * n2
    print(f'{n1} * {n2} = {result}')
    return [result, index]


myDict = {}

multiply(5, 5)
multiply(7, 9)

multiply = saveToDict(multiply)

for i in range(100):
    multiply(i + 5, i - 5, i)

for index, value in myDict.items():
    print(index, value)
