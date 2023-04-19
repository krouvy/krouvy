class ParentException(Exception):
    def __init__(self, message):
        super().__init__(message)  # помним про вызов конструктора родительского класса

class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message):
        super().__init__(message)

try:
    raise ChildException("Сообщение")  # поднимаем исключение-наследник, передаём дополнительный аргумент
except ParentException as e:
    print(e)  # выводим информацию об исключении