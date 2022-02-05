from Dangote_Bank_Main_Class import *

import datetime

#  date and time was imported to help me understand the month  the account was opened.

y = datetime.date.today()
# print(y.strftime("Today is " + "%B"))
today = (y.strftime("%m"))


# This is the class section for the program


# this my savings account bank class
# i created it in a different folder to ease my work
class Savings(Bank):
    def __init__(self, balance, id_number, name, month, savings, current):
        super().__init__(savings, current)
        self.month = month
        self.name = "Dangote Bank"
        # self.capital = 1000000000000
        self.bank_account = BankAccount(balance, id_number, name, month)
        self.client = Client(id_number, name)


class BankAccount:
    def __init__(self, balance, id_number, name, month):
        self.client = Client(id_number, name)
        self.balance = balance
        self.month = month

    # This is the code that aids depositing money to other accounts
    def deposit(self, amount):
        # Method to depose money at the bank account
        self.balance = self.balance + amount
        return self.balance

    # This code aids withdrawing money from your account
    # This code also follows the rules in the questions we were given

    def withdraw(self, amount):
        # Method to withdraw money at the bank account
        if int(today) - self.month > 6:
            self.balance = self.balance + (self.balance * 0.03)
            print('Your present balance is $' + str(self.balance))
            find = int(input("How much do you want to withdraw? e.g(20)"))
            if self.balance < amount:
                print("You have insufficient funds")
            else:
                self.balance -= amount
                print("You have withdrawn $" + str(find) + ' from your account')
                print("Your new present balance is $" + str(self.balance))
        else:
            print('Your present balance is $' + str(self.balance))
            print("You can't withdraw till you have used 6 months. Thank you")

    # This function aids money transfer from one account to the other

    def transfer(self, amount):
        # Method to transfer money from another account to another
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("$" + str(amount) + " has been successfully transferred.")
            return self.balance
        else:
            print("You balance is insufficient to perform this transaction!")
            transfer = self.balance
            return transfer

    # This method helps to check your account balance
    def balance_info(self):
        # Method to check balance of the bank account
        return "Ledger available: $" + str(self.balance)


class Client:
    def __init__(self, id_number, name):
        self.id = id_number
        self.name = name
