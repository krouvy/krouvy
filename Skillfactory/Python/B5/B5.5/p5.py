def getIndexMass(data):
    index = data[0] / (data[1] / 100) ** 2
    return -index


data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]

print(data)
print(list(map(getIndexMass, data)))

print()

print(sorted(data, key=getIndexMass))
print(sorted(data, key=lambda x: x[0] / x[1] ** 2))
print(sorted(list(map(getIndexMass, data))))

