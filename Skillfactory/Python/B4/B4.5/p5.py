def do_it_twice(func):
    def wrapper(*args, **kwargs):
        print('Декоратор старт')
        func(*args, **kwargs)
        print('\nПерерыв\n')
        func(*args, **kwargs)
        print('Декоратор конец')

    return wrapper


@do_it_twice
def say_words(*args, **kwargs):
    print('Неименные переменные ', *args)
    print('\nИменные переменные')
    for pet, name in kwargs.items():
        print(pet, name)


say_words('Жопа', 1, [1, 3, 5], {'dog': 'rada', 'cat': 'murka'}, *{'dog': 'fila', 'cat': 'gosha'},
          **{'dog': 'bima', 'cat': 'kirsu'}, idiot='durak')
