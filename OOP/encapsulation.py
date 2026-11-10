#encapsulation -> hide internal details of an object from the outside world
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance #private attribute
    def deposit(self,amount):
        self.__balance += amount
        print(f'Deposited {amount}. New balance: {self.__balance}')
    def get_balance(self):
        print(f'Total Balance,{self.__balance}') 
a1=BankAccount('123456789',1000)
a1.deposit(500)
a1.get_balance()