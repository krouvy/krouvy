x = 3

def func():
    global x
    print(x)

    x = 100
    x += 5

print(func())
print('Глобальная переменная изменилась внутри функции', x)
