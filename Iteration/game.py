### You and your friend are in a team to write a two-player game, human against computer, 
### such as Tic-Tac-Toe / Noughts and Crosses. Your friend will write the logic to play 
### one round of the game, while you will write the logic to allow many rounds of play, 
### keep score, decide who plays, first, etc. The two of you negotiate on how the two parts 
### of the program will fit together, and you come up with this simple scaffolding 
### (which your friend will improve later)

# Your friend will complete this function
def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    is True, the human gets to play first, else the
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random 
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} "
        .format(human_plays_first, result))
    return result
    
def play():
    number_of_games = 0
    human_wins = 0
    computer_wins = 0
    draws = 0

    human_played_first = False

    keep_play = True
    while(keep_play):
        
        human_played_first = not human_played_first
        outcome = play_once(human_played_first)
        if outcome == -1:
            print("You win!")
            human_wins += 1
        elif outcome == 1:
            print("I win!")
            computer_wins += 1
        else:
            print("Game drawn!")
            draws += 1

        number_of_games += 1

        print("Scores: Human={0}, Computer={1}, Draws={2}".format(human_wins, computer_wins, draws))
        print("Human wins={0}%".format(human_wins / number_of_games * 100))

        again = input("Do you want to play again? [Yes/No]")
        if again.lower() != "yes":
            print("Goodbye")
            keep_play = False

if __name__ == "__main__":
    play()