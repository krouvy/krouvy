def mirror(a, res=0):
    print(a, res)
    return mirror(a // 10, res * 10 + a % 10) if a else res


mirror(75473)