class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    def moneyX(self):
        ad = input(f'введи сумму для добавления: ')
        return f'balance: {self.__balance + int(ad)}'

    def __jackpot(self):
        jackpott = 10
        return f'jackpot: {self.__balance * jackpott}'

    def _united(self):
        _united = self.__balance
        friendsbalance = 100
        return f'steal: {self.__balance + friendsbalance}'

    def _kill(self):
        null = self.__balance - self.__balance
        return f'null: {null}'
    def print(self):
        return f'{Bank._kill(user)}\n' \
               f'{Bank._united(user)}'
    def __str__(self):
        return f'name: {self.__name} -- balance: {self.__balance}'

user = Bank('Nailya', 100)
print(user)
print(Bank.moneyX(user))
print(Bank.print(user))
# print(dir(Bank))



class Calculator(object):
    def __init__(self, arg1, arg2, calculator):
        self.arg1 = arg1
        self.arg2 = arg2
        self.calculator = calculator
    def __add__(self, arg1, arg2):
        return self.arg1 + self.arg2

    def __sub__(self, arg1, arg2):
        return self.arg1 - self.arg2

    def __mul__(self, arg1, arg2):
        return self.arg1 * self.arg2

    def __truediv__(self, arg1, arg2):
        return self.arg1 // self.arg2

    def __str__(self):
        return f'{self.calculator} is working!'

if __name__ == '__main__':
    c = Calculator(12, 10, 'calculator')
    print(c.__str__())
    print(c.__add__(12, 10))
    print(c.__sub__(12, 10))
    print(c.__mul__(12, 20))
    print(c.__truediv__(12, 10))
