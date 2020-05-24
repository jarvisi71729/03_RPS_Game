from random import randint


def int_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print("You did not enter a number between {} and {}".format(low, high))
        except ValueError:
            print("Invalid input")


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response")


def outcomes(user, computer):
    if user == computer:
        result = "Draw"

    elif user == "Paper" and computer == "Rock":
        result = "(1) User wins"

    elif user == "Rock"[0] and computer == "Scissors":
        result = "(2) User wins"

    elif user == "Scissors"[0] and computer == "Paper":
        result = "(3) User wins"

    else:
        result = "User loses"

    return result

# list of play choices
t = ["Rock", "Paper", "Scissors", "R", "P", "S"]

# computer range of choices
computer = t[randint(0, 2)]

keep_going = ""
while keep_going == "":

    print(computer)
    user = input("Rock, Paper, Scissors, Shoot! ").capitalize()
    print(outcomes(user, computer))

    keep_going = input("\nPress <enter> to play again or any key to stop. ")
