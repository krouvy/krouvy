a = 0
b = 0

z = set()

while a is b:
    print(id(a), a)
    a -= 1
    b -= 1
    z.add(a)
    print(z)

z.add(a)
print(id(a), id(b))
print(a)
print(z)
