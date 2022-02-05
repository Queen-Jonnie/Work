# Below I started by importing the class I created in the file Question__1a then I created a list and objects.


from Question__1a import Clients
ClientList = []
Client1 = Clients("Jessica", "01344", "Teacher", "0")
Client2 = Clients("Bonnie", "0245", "Lawyer", "0")
ClientList.append(Client1)
ClientList.append(Client2)

# The line of code below gives the user a choices of operation to pick from.


def Menulist():
    int(input(" To Withdraw money. Press 1. \n "
              "To View account balance. Press 2. \n "
              "To deposit money. Press 3. \n "
              "To Transfer Money. Press 4 \n "))

# This function below is for when the customer chooses to deposit money.


def Deposit():
    print("Hello Customer")
    amount = str(input("Enter the amount you want to deposit"))
    print("You have successfully deposited"+" "+amount)
    print("Your new balance is" + amount)

# This function below is for when the customer chooses to withdraw money.


def Withdrawal():
    A = int(input("How much are you willing to withdraw"))
    print("You have Successfully withdrawn " + str(A))

# This function below is for when the customer chooses to view their account balance.


def View():
    for items in ClientList:
        print("Your account Balance is"+" "+str(0))

# This function below is for when the customer chooses to transfer their account to another client.


def Transfer():
    print("How much are you willing to transfer")
    Number = int(input("Enter the Person's account number"))
    Much = int(input("How much would be transferred"))
    print(str(Much)+" "+"has been transferred to account owner"+" "+str(Number))
