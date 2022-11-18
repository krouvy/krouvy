def chet(L):
    return L % 2 == 0


L = [-2, -1, 0, 1, -3, 2, -3]

print(list(filter(chet, L)))
