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


# to invite the user to the game
print("Welcome to Hangman")
name = input("What is your name?")
print("Hello " + name + " Good luck!!!")

# This function 'main' acts as an encasing function for the hangman game code and also a looping agent\n
# for when the user wants to play again.


def main():
    tries = 0
    Right = 0
    guess = int(input("When was ALU founded?"))
    if guess in word_list:
        print("congrats!")
        Right += 1
    else:
        tries += 1
        print("you are hanging the man")

    guess = input("Who is the CEO of ALU")
    if guess in word_list:
        print("congrats!")
        Right += 1
    else:
        tries += 1
        print("you are hanging the man")

    guess = input("Where are ALU campuses?")
    if guess in word_list:
        print("congrats!")
        Right += 1
    else:
        tries += 1
        print("you are hanging the man")

    guess = int(input("How many campuses does ALU have?"))
    if guess in word_list:
        print("congrats!")
        Right += 1
    else:
        tries += 1
        print("you are hanging the man")

    guess = input("What is the name of ALU Rwanda's Dean?")
    if guess in word_list:
        print("congrats!")
        Right += 1
    else:
        tries += 1
        print("you are hanging the man")

    guess = input("Who is in charge of Student Life?")
    if guess in word_list:
        print("congrats!")
        Right += 1
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        print("You have lost the game")
        print("You got a total number of " + str(tries) + " wrong")
        print("You got a total number of " + str(Right) + " right")
        play_again = input("you want to play again?(y/n)")
        if play_again == "y":
            main()
        else:
            exit("Thanks for playing")

    guess = input("What is the name of our Lab?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:

        print("You have lost the game")

        print("You got a total number of " + str(tries) + " wrong")
        print("You got a total number of " + str(Right) + " right")
        play_again = input("you want to play again?(y/n)")
        if play_again == "y":
            main()
        else:
            exit("Thanks for playing")

    guess = int(input("How many students do we have in Year 2 CS?"))
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        print("you lose")
        print("You got a total number of " + str(tries) + " wrong")
        print("You got a total number of " + str(Right) + " right")
        play_again = input("you want to play again?(y/n)")
        if play_again == "y":
            main()
        else:
            exit("Thanks for playing")

    guess = int(input("How many degrees does ALU offer?"))
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        print("You lose")
        print("You got a total number of " + str(tries) + " wrong")
        print("You got a total number of " + str(Right) + " right")
        play_again = input("you want to play again?(y/n)")
        if play_again == "y":
            main()
        else:
            exit("Thanks for playing")
    guess = input("Where are the headquarters of ALU?")
    if guess in word_list:
        print("congrats!")
    else:
        tries += 1
        print("you are hanging the man")
    if tries == 6:
        print("You lose")
        print("You got a total number of " + str(tries) + " wrong")
        print("You got a total number of " + str(Right) + " right")
        play_again = input("you want to play again?(y/n)")
        if play_again == "y":
            main()
        else:
            exit("Thanks for playing")


main()
