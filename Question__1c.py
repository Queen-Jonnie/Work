# I started this file by importing all the code from the file Question__1b.


from Question__1b import *

#  Then I created a While loop to continue the operation.


answer = "yes"
while answer == "yes":

    Menulist()
    value = int(input("Enter your  number one more time: "))
    if value == 1:
        Withdrawal()

    if value == 2:
        View()

    if value == 3:
        Deposit()

    if value == 4:
        Transfer()
