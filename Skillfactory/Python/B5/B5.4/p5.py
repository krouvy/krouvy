def sumNums(n, s):
    print('Число S', s)
    if s < 0:
        return False
    elif n < 10:
        return n == s
    else:
        return sumNums(n // 10, s - n % 10)


print(sumNums(339, 14))
