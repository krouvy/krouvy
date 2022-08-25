login_list = [
    'root',
    'username1'
]

password_list = {
    'root': '1q2w3e4r',
    'username1': 'qwerty123'
}

username = input('Введите логин:\n')

if username in login_list:
    password = input('Введите пароль:\n')
    if password == password_list[username]:
        print('Добро пожаловать %s' % (username))
    else:
        print('Неверный пароль')
else:
    print('Вы не зарегистрированны')
