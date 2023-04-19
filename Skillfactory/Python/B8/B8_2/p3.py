class MyException(Exception):
    pass

try:
    raise MyException('Ошибка')
except MyException as e:
    print(e)
