def my_decorator(fn):
    def wrapper():
        fn()

    return wrapper  # возвращается задекорированная функция, которая заменяет исходную


# выведем незадерорированную функцию
def my_function():
    pass


# print(my_function)

resultFunction1 = my_decorator(my_function)
resultFunction2 = my_decorator(my_function)
print(resultFunction1, resultFunction2,)

@my_decorator
def my_function():
    pass


print(my_function)
