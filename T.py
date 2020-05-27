# Partially complete RPS comparison compile
# You can reuse this BUT you need to comment (and complete) it!!
# You can develop this further - it's very basic <just saying>

# wins

player_win_counter = 0
computer_win_counter = 0

def rps_outcome(user, comp):

    if user == comp:
        result = "It's a draw"

    elif user == "paper" and comp == "rock":
        result = "User wins"
        player_win_counter =+1

    elif user == "scissors" and comp == "paper":
        result = "User wins"
        player_win_counter +=1

    elif user == "rock" and comp == "scissors":
        result = "User wins"
        player_win_counter +=1

    else:
        result = "User Loses"
        computer_win_counter += 1
    return result

# **** Main Routine ****

comp_choice1 = "rock"
comp_choice2 = "paper"
comp_choice3 = "scissors"

user_list = ["rock", "paper", "scissor"]

for item in user_list:
    outcome = rps_outcome(item, comp_choice1)
    print("{} vs {}.  Result: {}".format(item, comp_choice1, outcome) )

    print(item, comp_choice2)

    print(item, comp_choice3)