list_ = [-5, 2, 4, 8, 12, -7, 5]

min_ = None
minIndex = None

for i, value in enumerate(list_):
    if value < 0:
        min_ = value
        minIndex = i
print(min_, minIndex)