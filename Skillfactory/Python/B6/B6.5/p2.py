class Opa:
    def __init__(self):
        self.odin = 1
        self._dva = 2
        self.__tri = 3


value = Opa()

for i in dir(value):
    print(i)
