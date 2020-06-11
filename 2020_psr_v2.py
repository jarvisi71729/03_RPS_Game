import random


# colour list (shortens code / makes code tidier)
# mention previous code trialing & error (colour) on slides

# def hl_statement(statement, char):
#     print()
#     print(char * len(statement))
#     print(statement)
#     print(char * len(statement))
#     print

# red: error messages
red = "\u001b[31m"

green = "\u001b[32m"

gold = "\u001b[33m"

dblue = "\u001b[34m"

pink = "\u001b[35m"

lblue = "\u001b[36m"

grey = "\u001b[37m"

colour_end = "\u001b[0m"

rainbow = ["red", "green", "gold", "dblue", "pink", "lblue", "grey"]
# china = hl_statement("pp", "p")


def int_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print(u"{}You did not enter a number between {} and {}{}".format(red, low, high, colour_end))
        except ValueError:
            print(u"{}Invalid input{}".format(red, colour_end))


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print(u"{}Sorry that is not a valid response{}".format(red, colour_end))


# player_wins = 0
# computer_wins = 0


def outcomes(user, computer):
    player_wins = 0
    computer_wins = 0

    if user == computer:
        result = u"{}Draw{}".format(gold, colour_end)

    elif user == "paper" and computer == "rock":
        result = u"{}User wins{}".format(green, colour_end)
        player_wins += 1

    elif user == "rock" and computer == "scissors":
        result = u"{}User wins{}".format(green, colour_end)

    elif user == "scissors" and computer == "paper":
        result = u"{}User wins{}".format(green, colour_end)

    else:
        result = u"{}User loses{}".format(pink, colour_end)
        computer_wins += 1
    return result

# list of play choices
game_items = ["rock", "paper", "scissors"]

# set player to False
player = False

# ftw = first to reach 'x' wins, starts a "rounds" loop
# ftw = int_check("First to reach *1 - 10* wins: ", 1, 10)


while player is False:

    # computer range of choices
    computer = random.choice(game_items)

    print("{}{}{}".format(grey, computer, colour_end))
    user = string_checker(u"{}Rock, Paper, Scissors, Shoot!{} ".format(dblue, colour_end), game_items)
    print(outcomes(user, computer))
