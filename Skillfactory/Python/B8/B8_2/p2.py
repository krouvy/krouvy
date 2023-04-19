class MyException(Exception):
    def __init__(self, num):
        self.num = num

    def delu(self):
        print(17 // self.num)

try:
    A = MyException(0)
    A.delu()
except MyException as e:
    print(e)
