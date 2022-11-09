def saveToDict(fn, myDict):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)

        if myDict == {}:
            myDict[0] = result
        else:
            newIndex = list(myDict)[-1] + 1
            myDict[newIndex] = result

    return wrapper

def multiply(n1, n2):
    result = n1 * n2
    print(f'{n1} * {n2} = {result}')
    return result

myDict = {}
myDict2 = {5: 'none'}

multiply(5, 5)
multiply(7, 9)
print(myDict2)

multiply = saveToDict(multiply, myDict2)

multiply(5, 5)
multiply(7, 9)
multiply(786, 9456)
print(myDict2)
