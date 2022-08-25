a = 42
b = 41

if a > b:
    result = a
else:
    result = b

print(result)
result = a if a > b else b
print(result)