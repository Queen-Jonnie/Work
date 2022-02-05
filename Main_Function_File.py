
from Current_Functions import *
from Savings_Functions import *

print("=============== WELCOME TO THE DANGOTE BANK ===============")
Dangote_input = int(input("""Operation you want to perform: 
                            1. Create an account
                            2. Perform transaction 
                            3. Exit the app
                            Please select your choice: """))
if Dangote_input == 1:
    ask = input("""What type of account do you want to open? "
                1. Current Account
                2. Savings Account
                """)
    if ask == "1":
        create_current()
    elif ask == "2":
        create_savings()
    else:
        print("Please, you can only select between 1 and 2!")
        print("Please, try again!")
        ask = input("""What type of account do you want to open?
                        1. Current Account
                        2. Savings Account
                        """)
        if ask == 1:
            create_current()
        elif ask == 2:
            create_savings()
elif Dangote_input == 2:
    ask_2 = input("""What type of account do you want to perform the transaction on?
        1. Current Account
        2. Savings Account
        """)
    if ask_2 == "1":
        account_id = int(input("Please insert your account id: "))
        selected_account = account_holder[account_id]
        print("Welcome to our service, " + selected_account.client.name + "!")
        run_operation_current(selected_account)
    elif ask_2 == "2":
        account_id = int(input("Please insert your account id: "))
        selected_account = account_holder[account_id]
        print("Welcome to our service, " + selected_account.client.name + "!")
        run_operation_savings(selected_account)
