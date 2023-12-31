'''Implement a class called BankAccount that represents a bank account
The class should private attributes account balance,account holder name,account balance 
Include methods deposit money, withdraw money, display account balance
Ensure that the account balance cannot accessed directly class to create instance of bank account and withdrawal functoinality'''

class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number=account_number
        self.__account_holder_name=account_holder_name




        self.__account_balance=initial_balance


  def deposit(self,amount):
    if amount>0:
        self.__account_balance+=amount 

        print("Deposited â‚¹{}.New balance:â‚¹{}.".format(amount,self.__account_balance)) 
    else:
        print("Invalid deposit amount.Please deposit a positive amount. ")
  def withdraw (self,amount):
    if amount>0 and amount<=self.__account_balance:
        self.__account_balance -= amount
        print("withdraw â‚¹{}".format(amount,self.__account_balance))
    else:
        print("Invalid withdrawal amount or insufficient")
  def display_balance(self):
    print("Account balance for{}(Account #{}):â‚¹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
#create an instance of the BankAccount class
account=BankAccount(account_number="1234567899",account_holder_name="A. Anbuchelvam ", initial_balance=15000.0)

#test deposit and withdrawal function
account.display_balance()
account.deposit(2000.0)
account.withdraw(500.0)
account.withdraw(1500.0)
account.display_balance()
