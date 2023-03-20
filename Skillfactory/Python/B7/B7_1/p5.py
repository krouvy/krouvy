class Dog:
    __happiness = 10
    _lucky = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле - шкала счастья
    @property
    def happiness(self):
        return self.__happiness

    # с помощью декоратора setter мы можем неявно передать во второй аргумент значение, находящееся справа от равно, а не закидывать это значение в скобки, как мы это делали ранее, когда не знали о декораторах класса
    @happiness.setter
    def happiness(self, value):  # допустим мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
        if value <= 100 and value >= 0:
            self.__happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
# print(jane.__happiness)
print(jane._lucky)
jane._lucky = 999
print(jane._lucky)
# jane.__happiness = 904
# print(jane.__happiness)

jane.happiness = 28
print(jane.happiness)
# print(jane.__happiness)

jane.happiness = 280