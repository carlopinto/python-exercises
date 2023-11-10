'''
Number Guessing Game
'''

import random

def show_score(attempts_list):
    if not attempts_list:
        print("There is currently no high score, it's yours for the taking!")
    else:
        min_value = min(attempts_list)
        if min_value == 1:
            print(f"The current high score is 1 attempt")
        else:
            print(f"The current high score is {min_value} attempts")

def start_game(lb, ub):
    attempts_list = []
    attempts = 0
    rand_num = random.randint(lb, ub)
    print("Hello! Welcome to the game of guesses.")
    player_name = input("What is your name? ")
    want_play = input(f"Hi {player_name}, would you like to play the guessing game? (Enter Yes/No): ")

    if want_play.lower() != "yes":
        print("Ok, thanks!")
        exit()
    else:
        show_score(attempts_list)

    while want_play.lower() == "yes":
        try:
            guess = int(input(f"Pick a number between {lb} and {ub}: "))
            if guess < lb or guess > ub:
                raise ValueError("Please guess a number within the given range.")
            
            attempts += 1
            
            if guess == rand_num:
                print("Nice. You got it!")
                print(f"It took you {attempts} attempts")
                want_play = input("Would you like to play again? (Enter Yes/No): ")
                if want_play.lower() != "yes":
                    print("Ok, have a good one!")
                    break
                else:
                    attempts_list.append(attempts)
                    attempts = 0
                    rand_num = random.randint(lb, ub)
                    show_score(attempts_list)
                    continue
            else:
                if guess > rand_num:
                    print("It's lower")
                elif guess < rand_num:
                    print("It's higher")

        except ValueError as err:
            print("Oh no! That is not a valid value. Try again...")
            print(err)

if __name__ == "__main__":
    start_game(1, 100)