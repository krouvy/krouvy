def len_int (x):
    if x == 0:
        return 1
    len_ = 0
    while x:
        x //= 10
        len_  += 1
    return (len_)

f = 653457
g = 123493

z = f**g

print(len_int(z))