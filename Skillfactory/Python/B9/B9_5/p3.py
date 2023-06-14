def flatten(a_list: list, depth: int = 0) -> list:
    count = 0
    while True:
        result = []
        has_list = False
        for element in a_list:
            if type(element) is list:
                result.extend(element)
                has_list = True
            else:
                result.append(element)
        a_list = result
        count += 1
        if not has_list or (0 < depth == count):
            break
    return result


class binaryTree:
    def __init__(self, value, index=0):
        self.index = index
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = binaryTree(next_value, self.index + 1)
        else:
            new_child = binaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = binaryTree(next_value, self.index + 1)
        else:
            new_child = binaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def printAllValues(self):
        print(self.value, self.index)
        if self.left_child is not None:
            print('<- ', sep='', end='')
            self.left_child.printAllValues()
        if self.right_child is not None:
            print('-> ', sep='', end='')
            self.right_child.printAllValues()

    def getStructure(self):
        childsValue = []
        if self.left_child is None:
            childsValue.append(self.left_child)
        else:
            childsValue.append(self.left_child.value)
        if self.right_child is None:
            childsValue.append(self.right_child)
        else:
            childsValue.append(self.right_child.value)

        structure = [{self.index: [self.value, childsValue]}]
        if self.left_child is not None:
            structure.append(self.left_child.getStructure())
        if self.right_child is not None:
            structure.append(self.right_child.getStructure())
        return structure


# A_node = binaryTree(0).insert_left(1).insert_right(2)
# A_node.left_child.insert_left(3).insert_right(4)
# A_node.right_child.insert_left(5).insert_right(6)
# print(A_node.value)
# print(A_node.left_child.value, A_node.right_child.value)
# print(A_node.left_child.left_child.value, A_node.left_child.right_child.value, A_node.right_child.left_child.value, A_node.right_child.right_child.value)

A_node = binaryTree(2).insert_left(7).insert_right(5)
A_node.left_child.insert_left(2).insert_right(6)
A_node.left_child.right_child.insert_left(5).insert_right(11)
A_node.right_child.insert_right(9)
A_node.right_child.right_child.insert_left(4)
A_node.right_child.right_child.insert_right(17)

# A_node.printAllValues()
# print(A_node.printAllValues())
La = A_node.getStructure()
print(La)
res = flatten(La, 5)
res = sorted(res, key=lambda d: list(*d.items())[0])
max = list(max(res, key=lambda d: list(*d.items())[0]).keys())[0] + 1
print(max)
print(res)

for i in range(0, max):
    counter = 0
    branches = []
    for j in res:
        if list(j)[0] == i:
            if counter == 0:
                print((12 - i) * '  ', f'({j[i][0]})', end='')
                branches.append(j[i][1])
                # if not i == 0:
                #     print((11 - i) * '  ', ' /', end='')
                counter += 1
            else:
                print('', f'({j[i][0]})', (max-i - 1) * ' ', end='')
                branches.append(j[i][1])
                # print(' \\', end='')

    if i == 0:
        print('\n', (11 - i) * '  ', f' / \\', end='')
    else:
        print()
        print((11 - i) * '  ', end='')
        for branch in branches:
            print(' ', end='')
            if branch[0] == None:
                print('  ', end='')
            else:
                print(' ', '/', end='')
            if branch[1] == None:
                print('  ', end='')
            else:
                print('', '\\', end='')
    print()
