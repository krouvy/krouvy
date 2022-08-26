num1 = int(input('Длина лесенки '))
for i in range(1, num1):
    print('@' * (num1 - i) + ('X' * i) + 'X' * (i - 1) + '@' * (num1 - i))
