a = 0
b = 0

while a is b:
    print(id(a), a)
    a -= 1
    b -= 1

print(id(a), id(b))
print(a)
