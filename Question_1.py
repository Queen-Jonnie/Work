# This is the word list from where the answers for the hangman game will come from.
word_list = [
    2015,
    "Fred Swaniker",
    "Rwanda and Mauritius",
    2,
    "Dr, Gaidi Faraj",
    "Sila Ogidi",
    "Madagascar",
    94,
    8,
    "Mauritius"
]

# Here we are defining the variables 'Right'(for when they get the question correct) and \n
# 'tries'(for when they get a question wrong).

Right = 0
tries = 0

# This function below after called, will greet the user when they input their name.


def greet(name):
    print("Hello " + name + " welcome to hangman and good luck!")


user_name = input("What is your name?")
greet(user_name)

# This functions below when called, will check when guess is returned whether the user's guess is in the word_list\n
# or not and will print out the appropriate responses while consecutively adding to the 'Right' or 'tries' variable.


def alu(guess):
    if guess in word_list:
        print("congrats!")


def check(guess):
    if guess not in word_list:
        print("Wrong")

    return guess


guess1 = int(input("When was ALU founded?"))
if alu(guess1):
    Right += 1
else:
    check(guess1)
    tries += 1
guess2 = input("Who is the CEO of ALU")
if alu(guess2):
    Right += 1
else:
    check(guess2)
    tries += 1

guess3 = input("Where are ALU campuses?")
if alu(guess3):
    Right += 1
else:
    check(guess3)
    tries += 1
guess4 = int(input("How many campuses does ALU have?"))
if alu(guess4):
    Right += 1
else:
    check(guess4)
    tries += 1
guess5 = input("What is the name of ALU Rwanda's Dean?")
if alu(guess5):
    Right += 1
else:
    check(guess5)
    tries += 1
guess6 = input("Who is in charge of Student Life?")
if alu(guess6):
    Right += 1
else:
    check(guess6)
    tries += 1
    if tries == 6:
        exit("You lost")
guess7 = input("What is the name of our Lab?")
if alu(guess7):
    Right += 1
else:
    check(guess7)
    tries += 1
    if tries == 6:
        exit("You lost")
guess8 = int(input("How many students do we have in Year 2 CS?"))
if alu(guess8):
    Right += 1
else:
    check(guess8)
    tries += 1
    if tries == 6:
        exit("You lost")
guess9 = int(input("How many degrees does ALU offer?"))
if alu(guess9):
    Right += 1
else:
    check(guess9)
    tries += 1
    if tries == 6:
        exit("You lost")
guess10 = input("Where are the headquarters of ALU?")
if alu(guess10):
    Right += 1
else:
    check(guess10)
    tries += 1
    if tries == 6:
        exit("You lost")
