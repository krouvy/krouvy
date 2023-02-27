class Human:

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age,
                                  int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age


h = Human()
h.age = -421
print(h.age)

h.set_age(15)
print(h.get_age())
