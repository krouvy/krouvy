num = int(input('Введи любое число '))
while True:
    if num % 2 == 0:
        num //= 2
    else:
        num = (num * 3 + 1) // 2
    print(num)
    if num == 1:
        break
