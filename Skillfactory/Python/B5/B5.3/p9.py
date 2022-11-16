L = "aaabbccccdaa"

last = L[0]
count = 0
result = ''

for i in L:
    if i == last:
        count += 1
    else:
        result += last
        result += str(count)
        last = i
        count = 1

result += last
result += str(count)

print(result)
