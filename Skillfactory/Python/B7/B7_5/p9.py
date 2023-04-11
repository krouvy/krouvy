class Balance():
    def __init__(self, balance=100):
        self.balance = balance

    @classmethod
    def getBalance(cls):
        return 'Ура'


print(Balance.getBalance())
