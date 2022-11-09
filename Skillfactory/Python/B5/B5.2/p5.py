z = set()

a = [1, 2, 3]

b = a.copy()

z.add(a)
z.add(b)

print(id(a), id(b), z)
