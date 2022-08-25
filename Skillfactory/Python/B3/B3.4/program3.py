
cord = list(map(int, (input('x,y = ').split())))
x = cord[0]
y = cord[1]

if x > 0 and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
else:
    print('На осях')
