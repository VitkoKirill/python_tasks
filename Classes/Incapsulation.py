class BankAccount():
    def __init__(self, _balance, _owner):
        if _balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = _balance
        self._owner = _owner

    def deposit(self, amount):
        self._balance += amount
        print(f'{self._owner} deposited {amount}, total balance: {self._balance}')

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f'{self._owner} withdrawn {amount}, total balance: {self._balance}')
        else:
            raise ValueError(f'{self._balance} is less than {amount}')

    def check_balance(self):
        print(f'{self._owner} balance: {self._balance}')


alfa_bank_account = BankAccount(1000, 'Nick')
alfa_bank_account.deposit(500)
alfa_bank_account.check_balance()
alfa_bank_account.withdraw(500)

t_bank_account = BankAccount(500, 'Sam')
t_bank_account.check_balance()
t_bank_account.withdraw(500)
alfa_bank_account.check_balance()
