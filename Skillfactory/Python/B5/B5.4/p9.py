yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"
USERS = ['krouvy', 'reason', 'lesson', 'albu']


def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")

    return wrapper


def login(func):
    def wrapper():
        login = input('Введите логин ')
        if login in USERS:
            func()
        else:
            print("Неверный логин")

    return wrapper


@is_auth
@login
def getData():
    dataBase = '1010101010101010101'
    print(dataBase)


getData()
