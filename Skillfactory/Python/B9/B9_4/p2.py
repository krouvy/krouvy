def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if any([s == "(", s == "[", s == "{"]):  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif any([s == ")", s == ']', s == '}']):
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and any(
                    [stack[-1] == "(" and s == ')',
                     stack[-1] == '[' and s == ']',
                     stack[-1] == '{' and s == '}']):
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0


string = '{[]()}'
print(par_checker(string))
