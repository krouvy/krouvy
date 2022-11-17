def findMin(array, min=None):
    if min == None:
        min = array.pop(0)

    if len(array) == 0:
        return min

    if min > array[0]:
        min = array.pop(0)
        min = findMin(array, min)
    else:
        array.pop(0)
        min = findMin(array, min)

    return min


L = [1, 6, -87, 4, 5, 7, -2, 7]

print(findMin(L))
