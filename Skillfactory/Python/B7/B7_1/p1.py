class Foo:

    @staticmethod  # помечаем метод который мы хотим сделать статичным декоратором @staticmethod
    def bar():
        print("bar")

    def hello():
        print('hello')

class Doo(Foo):
    def __init__(self):
        print('Doo создался')

Doo.bar()
D = Doo()
D.bar()

