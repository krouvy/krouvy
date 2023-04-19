class ParentException(Exception):  # создаём пустой класс – исключение потомка, наследуемся от exception
    errorMesage = 'Ошибка родителя'
    pass


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass


try:
    raise ChildException('Что?')  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e, e.errorMesage)  # выводим информацию об исключении
