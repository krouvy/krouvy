def fi(i):
    if i <= 1:
        return i
    return fi(i-1) + fi(i-2)


print(fi(3))
