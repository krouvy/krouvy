import inspect


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def process(character):
    nextOption = input('\nвыберете действие ')
    nextOption = nextOption.replace('(', '|').replace(')', '')
    nextOption = nextOption.split('|')

    actions = dir(character)

    if len(nextOption) == 1:
        if nextOption[0] in actions:
            variable = getattr(character, nextOption[0])
            if not callable(variable):
                print(f'{nextOption[0]}={variable}')
            else:
                print('Это не свойство, это метод')
        else:
            print('В этом классе нет такого свойства')
    else:
        nextOption[1] = nextOption[1].replace('"', '').replace("'", '')
        if nextOption[0] in actions:
            variable = getattr(character, nextOption[0])

            if callable(variable):
                args_method = variable.__code__.co_argcount - 1

                if ',' in nextOption[1]:
                    args_string = nextOption[1].split(',')

                    while '' in args_string:
                        args_string.remove('')

                    if args_method >= len(args_string):
                        variable(*args_string)
                    else:
                        print('Слишком много аргументов, требуется всего',
                              len(get_default_args(variable)) + args_method - len(get_default_args(variable)))
                else:
                    if nextOption[1] == '':
                        if len(get_default_args(variable)) == 0 and args_method != 0:
                            print('Данный метод требует', args_method, 'аргумента')
                        elif args_method - len(get_default_args(variable)) > 0:
                            print('Данный метод требует хотя бы', args_method - len(get_default_args(variable)),
                                  'аргумента. В идеале',
                                  len(get_default_args(variable)) + args_method - len(get_default_args(variable)))
                        else:
                            variable()

                    elif args_method - len(get_default_args(variable)) >= 0 and len(get_default_args(variable)) != 0:
                        variable(nextOption[1])
                    else:
                        print('Данный метод требует', args_method - len(get_default_args(variable)),
                              'аргумента.')
            else:
                print('Это не метод')
        else:
            print('У этого класса нет такого метода')


class Process:
    gameProcess = 3

    def __init__(self):
        self.name = input('Назовите первого своего персонажа ')
        self.character = Player(self.name)
        self.personList = [self.character]

    def createNewPerson(self):
        self.name = input('Назовите своего персонажа ')
        self.character = Player(self.name)
        self.personList.append(self.character)

    def selectPerson(self):
        for i in self.personList:
            print(i.name, i.hp)
        number = input('Введите номер персонажа ')
        if number.isdigit():
            number = int(number)
        else:
            print('Число содержит символы')
            self.selectPerson()

        if number in range(0, len(self.personList)):
            self.name = self.personList[number].name
            self.character = self.personList[number]
        else:
            print('Неверное число')
            self.selectPerson()

    def start(self):
        if (self.character.hp > 0):
            print('Жизней', self.gameProcess, 'из 3')
            self.gameProcess -= 1
            while self.character.hp:
                print('HP', self.character.hp, self.character.name)
                process(self.character)
        else:
            print(self.name, 'мертв, создайте нового персонажа')


class Player(Process):

    def __init__(self, name):
        self.name = name
        self.hp = 100

    def move(self, direction='вперед'):
        print(self.name, 'Пошел', direction)

    def punch(self, action, damage):
        print(f'{self.name} {action} на {damage} урона ')

    def death(self):
        self.hp = 0
        print(self.name, 'умер')

    def voice(self, emotion, action='сказал', words='привет'):
        print(self.name, emotion, action, words)

    def jump(self):
        print('Прыжок')


session = Process()

while session.gameProcess > 0:
    process(session)
