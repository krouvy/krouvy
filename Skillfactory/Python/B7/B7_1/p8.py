try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Перед исключением")  # теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b  # здесь может возникнуть исключение деления на ноль
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)  # Выводим информацию об ошибке
    print("После исключения")

except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)  # Выводим информацию об ошибке
    print("После исключения")

print("После После исключения")
