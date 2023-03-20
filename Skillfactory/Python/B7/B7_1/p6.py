class ParentClass:

    @classmethod
    def method(cls, arg):
        # print(cls, arg)
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


# # Вызываем методы класса через класс.
print('Тест 1')
D = ParentClass()

ParentClass.method(17)
ParentClass.call_original_method()  # ParentClassclassmethod. 5

print('ParentClass.call_class_method()', 'error')
# ParentClass.call_class_method()
D.method(197)
D.call_original_method()
D.call_class_method()

print('Тест 2')
my_obj = ChildClass()

ChildClass.method(17)
ChildClass.call_original_method()  # ParentClassclassmethod. 5

print('ChildClass.call_class_method()', 'error')
# ChildClass.call_class_method()

my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_original_method()
my_obj.call_class_method()  # ParentClassclassmethod. 10
