import random

listSongs = set()
while len(listSongs) != 10:
    listSongs.add(str(random.randint(1, 10)))

print(list(map(int, list(listSongs))))

border = (1, 10)
length = 10
a = []
if length <= border[1] - border[0] + 1:
    while len(a) != length:
        i = random.randint(border[0], border[1])
        if not a.count(i):
            a.append(i)

print(a)
