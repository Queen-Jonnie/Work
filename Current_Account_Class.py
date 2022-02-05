# Jessica Ayomide Bonnie.

from Dangote_Bank_Main_Class import *
from Current_Functions import *
# This is the class section for the program
# #bank is the parent of the current account
import datetime

# I imported the date and time to help me understand the month where the account was opened.

# this is my date and time in present day time
y = datetime.date.today()
# print(y.strftime("Today is " + "%B"))
today = (y.strftime("%m"))


# print('today is ' + today)

# this my my current account bank class
# i created it in a different folder to ease my work
class Current(Bank):
    def __init__(self, balance, idnumber, month, name, savings, current):
        super().__init__(savings, current)
        self.name = "Dangote bank"
        self.capital = 30000000000
        self.bank_account = BankAccount(balance, idnumber, name)
        self.client = Client(idnumber, name)
        self.month = month


class BankAccount:
    def __init__(self, balance, idnumber, name):
        self.client = Client(idnumber, name)
        self.balance = balance

    # This is the code that aids depositing money to other accounts
    def deposit(self, amount):
        # Method to depose money at the bank account
        self.balance = self.balance + amount
        return self.balance

    # This code aids withdrawing money from your account
    # Because when you input an amount more than the amount you have
    # The code will tell you you have insuffiecient amount
    # When you try to withdraw after one month
    # The code will let you withdraw plus your intrest
    def withdraw_current(self):
        account_id = int(input("Please insert your account id: "))
        selected_account = account_holder[account_id]
        print("Welcome to our service, " + selected_account.client.name + "!")
        if int(today) -self.month > 1:
            self.balance = self.balance + (self.balance * 0.01)
            print('Your present balance is $' + str(self.balance))
            find = int(input("How much do you want to withdraw? e.g(20)"))
            if self.balance < find:
                print("You have insufficient funds")
            else:
                self.balance -= find
                print("You have withdrawn $" + str(find) + ' from your account')
                print("Your new present balance is $" + str(self.balance))
        else:
            print('Your present balance is $' + str(self.balance))
            find = int(input("How much do you want to withdraw? e.g(20)"))
            if self.balance < find:
                print("You have insufficient funds")
            else:
                self.balance -= find
                print("You have withdrawn $" + str(find) + ' from your account')
                print("Your new present balance is $" + str(self.balance))

    # This function aids money transfer from one account to the other

    def transfer_Money(self, amount):
        # Method to transfer money from another account to another
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("$" + str(amount) + " has been successfully transferred.")
            return self.balance
        else:
            print("You balance is insufficient to perform this transaction!")
            transfer = self.balance
            return transfer

    def balance_check(self):
        # Method to check balance of the bank account
        return "Ledger available: $" + str(self.balance)


class Client:
    def __init__(self, idnumber, name):
        self.id = idnumber
        self.name = name
