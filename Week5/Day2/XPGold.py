# Exercise 1: Bank Account
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
class BankAccount:
    def __init__(self,balance,username,password,authenticated):
        self.balance=balance
        self.username=username
        self.password=password
        self.authenticated=authenticated
# balance - (an attribute)
# __init__ : initialize the attribute

# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
    def deposit(self,number):
        if authenticated=True:
            if number>0:
                self.balance+=number
            else:
                raise Exception('You must enter a number greater than 0')
        else:
            raise Exception("Your username or password were invalid")
        
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive
    def withdraw(self,number):
        
        if authenticated=True:
            if number>0:
                self.balance-=number
            else:
                raise Exception('You must enter a number greater than 0')
        else:
            raise Exception("Your username or password were invalid")
    
     def authenticate(self,username,password):
            if self.username==username and self.password==password:
            authenticated=True
        else:
            authenticated=False
# Part II : Minimum balance account

# Create a MinimumBalanceAccount that inherits from BankAccount.
class MinimumBalanceAccount(BankAccount):
    def __init__(self,balance,minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance=minimum_balance
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
    def withdraw(self,number):
        if self.balance-number>self.minimum_balance:
            self.balance-=number
        else:
            raise Exception (f"You can't withdraw ${number} since it will drop you below your minimum balance.")
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.


# Part III: Expand the bank account class

# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (default to False)

# Create a method called authenticate. This method should accept 2 strings a username and password. If the username and password match the instances username and password the method should set the authenticated boolean to True.
    # def authenticate(self,username,password):
    #     if self.username==username and self.password==password:
    #         authenticated=True
    #     else:
    #         authenticated=False
# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception
