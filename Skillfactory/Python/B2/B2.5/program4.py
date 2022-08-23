list1 = list(map(int,input('Введите список чисел ').split()))

list1[0], list1[-1], = list1[-1], list1[0]
list1.append(sum(list1))

print(list1)
