import time


def timeDecorator(fn):
    def wrapper():
        print(f'Функция{fn} запустилась')
        t0 = time.time()
        result = fn()
        t2 = time.time() - t0

        print(f"Функция выполнилась. Время: {t2:.10f}")
        return result

    return wrapper


def f1():
    return 6436436000 ** 12


def f2():
    return pow(6436436000, 12)


f1 = timeDecorator(f1)
f2 = timeDecorator(f2)

print('Мой код', f1(), f2())
