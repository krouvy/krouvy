def getInfinityArray(num1=1, n=1):
    while num1 < 1000000000:
        num1 = num1 + n
        # print(num1)
        yield num1

print(*getInfinityArray(1, 1000))

print('Другое сообщение')
