L = [int(input()) % 2 == 0 for i in range(5)]

print(any(L) and not all(L))
print(*zip(L))