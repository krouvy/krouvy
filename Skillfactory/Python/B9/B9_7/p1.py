def countIn(list, value):
    count = 0
    for i in list:
        if value == i:
            count += 1
    return count


L = [5, 5, 5, 3, 2, 8, 6, 1]
print(countIn(L, 4))
