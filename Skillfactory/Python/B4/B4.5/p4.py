def my_decorator_buklov(fn):
    def wrapper():
        print('Вызвылась функция декоратор')
        fn()
        print('Функция декоратор завершилась')

    return wrapper  # возвращается задекорированная функция, которая заменяет исходную


# выведем незадерорированную функцию
def function_hello():
    print('hello')
    pass


# выведем задерорированную функцию
@my_decorator_buklov
def function_decor():
    print('decor')
    pass


hello2 = my_decorator_buklov(function_hello)
hello2()  # вызвылась функция декоратор, hello, функция декоратор завершилась

print('///////////')

hello = function_hello()  # hello

print('///////////')

decor = function_decor()  # Вызвылась функция декоратор, decor, Функция декоратор завершилась
