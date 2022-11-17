def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

L = [1, 6, -87, 4, 5, 7, -2, 7]

print(min_list(L))