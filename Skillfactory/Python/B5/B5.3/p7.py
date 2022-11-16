L = [bool(int(input()) % 2) for i in range(5)]
print(not all(L), L)
L = [int(input()) % 2 == 0 for i in range(5)]
print(any(L), L)
