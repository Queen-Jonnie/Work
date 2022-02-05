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


# to invite the user to the game
print("Welcome to Hangman")
name = input("What is your name?")
print("Hello " + name + " Good luck!!!")


while True:
    tries = 0
    guess = int(input("When was ALU founded?"))
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = input("Who is the CEO of ALU")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = input("Where are ALU campuses?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = int(input("How many campuses does ALU have?"))
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = input("What is the name of ALU Rwanda's Dean?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = input("Who is in charge of Student Life?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = input("What is the name of our Lab?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = int(input("How many students do we have in Year 2 CS?"))
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = int(input("How many degrees does ALU offer?"))
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    guess = input("Where are the headquarters of ALU?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        break

    break
