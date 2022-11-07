def decor(x):
    def addFive(y):
        return x + y

    return addFive


n1 = decor(10)
print(n1)
print(n1(5))
print(n1(6))
