class AnimalHouse:
    def __init__(self, firstName, secondName, balance):
        self.firstName = firstName
        self.secondName = secondName
        self.balance = balance


    def getData(self):
        return f'Клиент "{self.firstName} {self.secondName}". Баланс:{self.balance}'


class Korporative(AnimalHouse):
    def __init__(self, firstName, secondName, balance, city, role):
        self.city = city
        self.role = role

        super().__init__(firstName, secondName, balance)

    def getDataKorporative(self):
        return f'{self.firstName} {self.secondName}", г.{self.city}, статус "{self.role}"'


ivan = Korporative('Иван', 'Петров', '117', 'Москва', 'Системный Администратор')
sergey = Korporative('Сергей', 'Васильев', '1200', 'Чебоксары', 'Инженер')

users = [ivan, sergey]

for user in users:
    print(user.getData())
    print(user.getDataKorporative())