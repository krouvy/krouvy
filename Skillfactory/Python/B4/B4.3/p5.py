d = {1, 2, 3, 4, 5, 6, 7}

d1 = {'m1': 1, 'm2': 2, 'm3': 3}

def it(**kwargs):
    print(kwargs)

# print(it('m1': 1, 'm2': 2, 'm3': 3))

print(it(**d1))
