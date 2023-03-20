
class C(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42

    def Print(self):
        print(self.__d)

    def getClassName(self):
        return '_' + self.__class__.__name__


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

    def getParrentClassName(self):
        return '_' + self.__class__.__bases__[0].__name__


object1 = D()
object2 = C()

print('Дочерний класс, обращается к своему свойству', object1.e)
print('Дочерний класс, обращается к свойству родителя', object1.c)

print('Родительский класс, обращается к свойству', object2.c)

print('Родительский класс обращается к своему привату', getattr(object2, object2.getClassName() + '__d'))

print('Дочерний класс обращается к привату родителя', getattr(object1, object1.getParrentClassName() + '__d'))
