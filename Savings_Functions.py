from Savings_Account_Class import *

# This file is for the function file related for Dangote bank


# This is a list of all clients at the bank

client_one = Savings(300000, 0, "Tope", 2, "savings", "Nil")
client_two = Savings(5000000, 1, "Mofe", 4, "Nil", "Current")
client_three = Savings(3400000, 2, "Deji", 5, "Savings", "Current")
client_four = Savings(651000, 3, "Derin", 3, "Savings", "Nil")
client_five = Savings(234566, 4, "Deolu", 7, "Savings", "Nil")
account_holder = [client_one, client_two, client_three, client_four, client_five]


def run_operation_savings(selected_account):
    # This is the function for asking clients of the bank what they wish to do

    service_choice = int(input(" Service Available For Savings Account\n"
                               "Please note that when you deposit you cannot withdraw until after a three month period\n"
                               "1 forWithdrawal\n"
                               "2 for Deposit\n"
                               "3 for Balance Check\n"
                               "4 for Transfer money\n"
                               "Select transaction of your choice"))

    if service_choice == 1:
        amount = int(input("How much do you want to withdraw? [number]: "))
        result = selected_account.bank_account.withdraw(amount)
        print("Ledger available: $" + str(result))
        restart(selected_account)
    elif service_choice == 2:
        amount = int(input("How much do you want to depose? [number]: "))
        result = selected_account.bank_account.deposit(amount)
        print("Ledger available: $" + str(result))
        restart(selected_account)
    elif service_choice == 3:
        print(selected_account.bank_account.balance_info())
        restart(selected_account)
    elif service_choice == 4:
        index = 0
        for x in account_holder:
            print(str(index) + ". " + x.client.name)
            index += 1
        transfer_person = int(input("Insert the account id: "))
        transfer_person = account_holder[transfer_person]
        amount = int(input("Insert the amount you want to transfer [number]: "))
        if transfer_person != selected_account:
            result_one = transfer_person.bank_account.deposit(amount)
            result_two = selected_account.bank_account.transfer(amount)
            print("Ledger available: $" + str(result_two))
        else:
            print("Please re-insert valid id account! (Not yours)")
            index = 0
            for x in account_holder:
                print(str(index) + ". " + x.client.name)
                index += 1
            transfer_person = int(input("Insert the account id: "))
            transfer_person = account_holder[transfer_person]
            amount = int(input("Insert the amount you want to transfer [number]: "))
            result_one = transfer_person.bank_account.deposit(amount)
            result_two = selected_account.bank_account.transfer(amount)
        restart(selected_account)
    else:
        print("Error: please try again!")
        run_operation_savings(selected_account)


def restart(selected_account):
    # This function serves as a while loop for the Program
    restart = input("Do you wish to perform another transaction?(yes/no): ")
    if restart == "yes":
        run_operation_savings(selected_account)
    else:
        exit("Thank your for using Dangote Bank!")


# for this function, it was all about helping the user create a new bank account

def create_savings():
    # This function will create a new bank account in the list
    balance = int(input("Insert the amount of money you wish to put in the new account: "))
    id_number = int(input("Insert an id corresponding to the new account [ex: 5, 6, ...]: "))
    name = input("Insert the name of the account holder: ")
    month = input("What month are you opening this account in?: (In numbers please (i.e january = 1) ")
    new_account = Savings(balance, id_number, name, month, Savings, "Nil")
    account_holder.append(new_account)
    print("Account created successfully!")
    ask = input("Do you want to perform another transaction?: (yes/no)").lower()
    if ask == 'yes':
        run_operation_savings(1)
    elif ask == 'no':
        exit("See you soon!!")
    else:
        exit("Bye!!")
