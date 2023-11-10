'''
Rock Paper Scissors
-------------------------------------------------------------
'''


import random
import os
import re

def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!\n')
                return False

        except ValueError as err:
            print(err)

def show_stats(scores):
    """"""
    if scores == [0, 0, 0]:
        print("There are currently no stats yet, this is your first game!")
    else:
        print("Ties: {0}, Wins: {1}, Losses: {2}".format(scores[1], scores[2], scores[0]))
    print()

def result(c1, c2):
    """ Given the two choices, return the result 
        0 for tie, -1 for c2, 1 for c1"""
    c1 = c1.upper()
    c2 = c2.upper()
    if c1 == c2:
        return 0
    elif c1 == "R" and c2 == "P": 
        print("Paper beats rock")
        return -1
    elif c2 == "R" and c1 == "P":
        print("Paper beats rock")
        return 1
    elif c1 == "R" and c2 == "S": 
        print("Rock beats scissors")
        return 1
    elif c2 == "R" and c1 == "S":
        print("Rock beats scissors")
        return -1
    elif c1 == "S" and c2 == "P": 
        print("Scissors beats paper")
        return 1
    elif c2 == "S" and c1 == "P":
        print("Scissors beats paper")
        return -1

def play_rps():
    scores = [0, 0, 0]
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors - Shoot!\n')

        show_stats(scores)

        user_choice = input('Choose your weapon [R]ock], [P]aper, or [S]cissors: ')

        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue
        
        choices = [('R', "Rock"), ('P', "Paper"), ('S', "Scissors")]

        user_choice_word = ""
        for (letter, word) in choices:
            if letter == user_choice.upper():
                user_choice_word = word

        print(f'You chose: {user_choice_word}')

        opp_choice_tuple = random.choice(choices)

        opp_choice = opp_choice_tuple[0]

        print(f'I chose: {opp_choice_tuple[1]}')

        res = result(user_choice, opp_choice)

        if res == 0:
            print('Tie!')
            scores[1] += 1
        elif res == -1:
            print('I win!')
            scores[0] += 1
        elif res == 1:
            print('You win!\n')
            scores[2] += 1

        play = check_play_status()
    
    show_stats(scores)


if __name__ == '__main__':
   play_rps()