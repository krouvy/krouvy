class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):  # печать с помощью обхода в ширину
        queue = [self]  # создаем очередь
        values = []  # значения в порядке обхода в ширину
        while queue != []:  # пока она не пустая
            last = queue.pop(0)  # извлекаем из начала
            if last is not None:  # если не None
                values.append("%d" % last.value)  # добавляем значение
                queue.append(last.left_child)  # добавляем левого потомка
                queue.append(last.right_child)  # добавляем правого потомка
            return ''.join(values)

    def search(self, x):
        if self.value == x:  # если нашли элемент,
            return self  # возвращаем ссылку на узел

        elif x < self.value:  # или, если значение меньше ключа, продолжаем
            return self.left_child.search(x)  # поиск в левом поддереве
        elif x > self.value:  # иначе в правом
            return self.right_child.search(x)
        else:  # если такое значение не нашлось,
            return False

    def minimum(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.minimum()

    def maximum(self):
        if self.right_child is None:
            return self
        else:
            return self.right_child.maximum()

    def next_value(self, x):
        current = self
        successor = None
        while current is not None:
            if current.value > x:
                successor = current
                current = current.left_child
            else:
                current = current.right_child
        return successor
