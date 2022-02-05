from Current_Account_Class import *

# This file is for the function file related FOR Dangote bank


# This is the list of  clients at the bank

client_one = Current(120000, 0, "Timi", 3, "Savings", "Nil")
client_two = Current(1000000, 1, "Taiwo", 6, "Nil", "Current")
client_three = Current(2000000, 2, "Kehinde", 4, "Nil", "current")
client_four = Current(9000000, 3, "Mariam", 7, "Nil", "Current")
client_five = Current(300000, 4, "Barakat", 1, "Nil", "Current")
account_holder = [client_one, client_two, client_three, client_four, client_five]


def run_operation_current(selected_account):
    # This is the main operation for the bank
    # The user interface which the user can withdraw, deposit and check balance

    service_choice = int(input(
        """-------------- Service Available --------------
                1. Withdrawal
                2. Deposit
                3. Balance Check 
                4. Transfer money 
          Select transaction of your choice: """))
    if service_choice == 1:
        amount = int(input("How much do you want to withdraw? [number]: "))
        result = selected_account.bank_account.withdraw(amount)
        print("Ledger available: $" + str(result))
        restart(selected_account)
    elif service_choice == 2:
        amount = int(input("How much do you want to deposit in number: "))
        result = selected_account.bank_account.deposit(amount)
        print("Ledger available: $" + str(result))
        restart(selected_account)
    elif service_choice == 3:
        print(selected_account.bank_account.balance_info())
        restart(selected_account)
    elif service_choice == 4:
        index = 0
        for x in account_holder:
            print(str(index) + ". " + str(x.client.name))
            index += 1
        transfer_person = int(input("Insert the account id: "))
        transfer_person = account_holder[transfer_person]
        amount = int(input("Insert the amount you want to transfer to the one of the number listed above: "))
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
        run_operation_current(selected_account)


def restart(selected_account):
    # This function serves as the while loop
    restart = input("Do you wish to perform another transaction?(yes/no): ")
    if restart == "yes":
        run_operation_current(selected_account)
    else:
        exit("Thank your for using Dangote Bank!")


# This function is for helping the user create a new bank account

def create_current():
    # This function will create a new bank account in the list
    balance = int(input("Insert the amount of money you wish to put in the new account: "))
    id_number = int(input("Insert an id corresponding to the new account [ex: 5, 6, ...]: "))
    name = input("Insert the name of the account holder: ")
    month = input("What month are you opening this account in?: (In numbers please (i.e january = 1) ")
    new_account = Current(balance, id_number, name, month, "savings", "current")
    account_holder.append(new_account)
    print("Account created successfully!")
    restart = input("Do you wish to perform another transaction?(yes/no): ")
    if restart == 'yes':
        run_operation_current("selected_account")
    else:
        exit("Thanks!")
