numbers = list(map(int, (input('a,b,c = ').split())))
a, b, c = numbers[0], numbers[1], numbers[2],

if a < 45 <= (b + c) // 2 or\
    b < 45 <= (a + c) // 2 or\
    c < 45 <= (a + b) // 2:
    print('True')
else:
    print('False')