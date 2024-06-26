class BankAccount:
    def __init__(self, account_number, balance):
        if type(account_number) == str and type(balance) == float:
            self._account_number = account_number
            self._balance = balance
        else:
            print('account_number=string & balance=float')

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        if type(account_number) == str:
            self._account_number = account_number
        else:
            raise TypeError('account_number=string')

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if type(balance) == float:
            self._balance = balance
        else:
            raise TypeError('balance=float')

    def deposit(self, amount):
        if type(amount) == float:
            self._balance = self._balance + amount
        else:
            print('amount should be float')

    def withdraw(self, amount):
        if type(amount) == float:
            if (self._balance - amount) >= 0:
                self._balance = self._balance - amount
            else:
                print("you dont have enough money!!")
        else:
            print('amount should be float')