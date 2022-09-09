def rec(i):
    if i == 1:
        return i
    else:
        return i * rec(i - 1)


print(rec(5))
