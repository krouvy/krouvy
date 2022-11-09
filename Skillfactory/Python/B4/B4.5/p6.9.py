def f(n):
    return n * 123456789


def cache(func):
    cache_dict = {}

    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f"Добавление результата в кэш: {cache_dict[num]}")
        else:
            print(f"Возвращение результата из кэша: {cache_dict[num]}")
        print(f"Кэш {cache_dict}")
        return cache_dict[num]

    return wrapper


newFoo = cache(f)

newFoo(1)
newFoo(2)
newFoo(3)
newFoo(4)
newFoo(17)
newFoo(4)
newFoo(-4)
