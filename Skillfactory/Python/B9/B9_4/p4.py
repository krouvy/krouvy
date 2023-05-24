def is_empty():
    return head == tail and queue[head] == 0


def size():
    if is_empty():
        return 0
    elif head == tail:
        return N_max
    elif head > tail:  # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else:  # или если хвост стоит правее начала
        return tail - head


def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max


def top():  # выводим приоритетную задачу
    print("Задача №%d в приоритете" % (queue[head]))

def last():  # выводим приоритетную задачу
    if not tail == head and tail == 0:
        print("Задача №%d в последняя в очереди" % (queue[N_max - 1]))
    else:
        print("Задача №%d в последняя в очереди" % (queue[tail - 1]))



def do():  # выполняем приоритетную задачу
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0  # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max  # и циклично перемещаем указатель


N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "top":
        if is_empty():
            print("Очередь пустая")
        else:
            top()
    elif cmd == "last":
        if is_empty():
            print("Очередь пустая")
        else:
            last()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")
