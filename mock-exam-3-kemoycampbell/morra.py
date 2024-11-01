"""
@author: <Your name>
date: <today's date>
Project code name: HandBattle
Purpose:
    A program that plays Morra
"""

import datetime
import random

# PREDEFINED BELOW, DO NOT MODIFY ANY CODE
LINE_SEPARATOR = "=============================="
HAND_MIN = 1
HAND_MAX = 3

"""
    This function will print the header containing 
    the game name, version number, and today's date and time
"""


def get_game_header():
    now = datetime.datetime.now()

    return \
        f"{LINE_SEPARATOR}" \
        "\nMorra" \
        "\n\tGame Version 1.0" \
        f"\n{LINE_SEPARATOR}" \
        f"\nDate and Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"


"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        game_round: The current round in the game

    returns the xp for the round
"""


def generate_xp(game_round):
    if game_round < 1:
        game_round = 1

    return random.randint(HAND_MIN, HAND_MAX) * game_round


"""
    This function will randomly pick a hand for the computer.
    This will return a hand from HAND_MIN (1) to HAND_MAX (3)
"""


def get_computer_hand():
    return random.randint(HAND_MIN, HAND_MAX)


"""
    This function will return a random hand sum guess for the computer.
    This will return a hand sum from HAND_MIN * 2 + HAND_MIN * 2
"""


def get_computer_guess():
    return random.randint(HAND_MIN, HAND_MAX) + random.randint(HAND_MIN, HAND_MAX)
# PREDEFINED ABOVE, DO NOT MODIFY ANY CODE


# STUDENT CODE HERE
# ...
def determine_winner(player_hand, player_guess, computer_hand, computer_guess) :
    winner = "player"

    #calculate the sum of the player's and computer fingers
    hands_sum = player_hand + computer_hand
    if player_guess == computer_guess and player_guess == hands_sum:
        winner = "tie"
    elif player_guess == computer_guess and player_guess!=hands_sum:
        winner = "no winner"
    elif player_guess!=hands_sum and computer_guess!=hands_sum:
        winner = "no winner"
    elif computer_guess == hands_sum:
        winner = "computer"
    
    return winner

def get_player_hand():
    while True:
        try:
            player_guess = int(input(f"Pick a number between {HAND_MIN}-{HAND_MAX}:"))
            if player_guess>=HAND_MIN and player_guess<=HAND_MAX:
                return player_guess
            print("Invalid choice!")
        except ValueError:
            print(f"you must pick a number between {HAND_MIN}-{HAND_MAX}!")
def get_player_guess():
    while True:
        try:
            player_guess = int(input(f"Guess the sum between {HAND_MIN*2}-{HAND_MAX*2}:"))
            if player_guess>=HAND_MIN*2 and player_guess<=HAND_MAX*2:
                return player_guess
            print("Invalid choice!")
        except ValueError:
            print(f"you must pick a number between {HAND_MIN*2}-{HAND_MAX*2}!")

def get_stats(player_score, player_win, computer_score,computer_wins):
    stats = f"Player Score:{player_score}\nPlayer wins:{player_win}\nComputer score:{computer_score}\nComputer wins:{computer_wins}"
    return stats

def get_play_again_prompt():
    while True:
        again = input("Do you want to play another round?(yes/quit):")
        if again!="yes" and again!="quit":
            print("Invalid choice!")
            continue 
        return again


#Testing my functions
# player_hand = 3
# computer_hand = 2
# sum_guess = player_hand + computer_hand

# player_guess = 3
# computer_guess =2

# winner = determine_winner(player_hand, player_guess, computer_hand, computer_guess)

# print(winner)

# get_player_hand()

# get_player_guess()

# player_score = 5
# player_wins = 20
# computer_score = 15
# computer_wins = 200
# stats = get_stats(player_score, player_wins, computer_score, computer_wins)
# print(stats)

# get_play_again_prompt()


def main():
    player_score = 0
    player_wins = 0
    computer_score = 0
    computer_wins = 0
    game_round = 1

    # STUDENT CODE HERE
    # ...
    print(get_game_header())
    while True:
        if game_round > 1:
            print("Players Stats\n==============")
            print(get_stats(player_score, player_wins, computer_score, computer_wins))
            print()
        
        print(f"Current round:{game_round}")

        computer_hand = get_computer_hand()
        computer_guess = get_computer_guess()
        player_hand = get_player_hand()
        player_guess = get_player_guess()

        print(f"Computer's hand:{computer_hand}")
        print(f"Computer's guess:{computer_guess}")
        print()

        print(f"The sum of both hands:{computer_hand+player_hand}")

        winner = determine_winner(player_hand, player_guess, computer_hand, computer_guess)
        print(f"winner:{winner}")
        if winner == "player":
            player_score+= generate_xp(game_round)
            player_wins+=1
        elif winner == "computer":
            computer_wins+=1
            computer_score+= generate_xp(game_round)
        
        another_round = get_play_again_prompt()
        print()
        if another_round == "yes":
            game_round+=1
        else:
            break
            
        
        

    print("Thank you for playing Morra!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was ended abruptly by the user\n")
