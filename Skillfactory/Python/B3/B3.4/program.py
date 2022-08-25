list1 = input('Введите список чисел ').split()

if len(list1) == len(set(list1)):
    print('Этот список уникален')
else:
    print('Есть повторяющиеся элементы')
