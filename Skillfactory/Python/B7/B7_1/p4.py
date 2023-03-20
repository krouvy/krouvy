class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3


jane = Dog("jane", 4)
print(jane.human_age)
print(jane.age)