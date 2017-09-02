# day4: property


class Account(object):
    def __init__(self, name):
        # self.__dict__['name'] = name
        self.__dict__['name'] = name
        self.__dict__['balance'] = 0
        self.trans = []

    def get_name(self):
        return self.__dict__['name']

    def set_name(self, name):
        # 17
        if not isinstance(name, str):
            raise Exception('name is not string')
        self.__dict__['name'] = name

        # 18
        # raise AttributeError('name is not allowed to set')

    name = property(get_name, set_name)

    @property
    def balance(self):
        # return sum(self.trans)
        return self.__dict__['balance']

    def deposit(self, amount):
        # self.balance += amount
        self.__dict__['balance'] += amount
        self.trans.append(amount)

    def withdraw(self, amount):
        # self.balance -= amount
        self.__dict__['balance'] -= amount
        self.trans.append(-amount)


b1 = Account('Joe')
print b1.name
b1.deposit(100)
b1.withdraw(10)
b1.withdraw(30)
print b1.balance
b1.name = 'Xu'
print b1.name









print 'all tests pass'
