class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

alex = User(mail='s@mail.ru', name='alex')
marlin = User('Marlin', 'm@mail.com')
print(alex.name, alex.mail)
print(marlin.name, marlin.mail)
print(marlin)
