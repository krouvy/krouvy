from contextlib import contextmanager


@contextmanager
def MyOpen(path, type):
    file = open(path, type, encoding='utf8')
    print('Файл открыт')
    yield file
    print('Файл закрыт')
    file.close()

with MyOpen('file', 'r') as file:
    file = file.read()
    print(file)