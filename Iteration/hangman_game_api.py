'''
Hangman Game
-------------------------------------------------------------
`httpx` package is required.
Since synchronous client is powered by `httpx.Client`.
'''


import random
import time
import os

# https://pypi.org/project/python-freeDictionaryAPI/
from freedictionaryapi.clients.sync_client import DictionaryApiClient
from freedictionaryapi import errors 


def play_again():
    question = '\nDo you want to play again? y = yes, n = no \n'
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)

    if play_game.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        return False


def hangman(word):
    display = '_' * len(word)
    
    # number of wrong guesses
    count = 0
    # max number of mistakes
    limit = 5
    letters = list(word)
    # use list of tuples to check if a letter has been guessed already 
    # - useful if the same letter occurs more than once within a word
    words_tuple = []
    for l in letters:
        words_tuple.append((l, False))
    guessed = []
    while count < limit:
        print(f'\nHangman Word: {display}')
        attempt = input("Do you want to guess a letter or word? [L]etter/[W]ord]: \n").strip()
        while attempt.lower() != "letter" and attempt.lower() != "word" and attempt.lower() != "l" and attempt.lower() != "w":
            print('Invalid input. Enter L/W or letter or word\n')
            attempt = input(f"Do you want to guess a letter or word? [L]etter/[W]ord]: \n").strip()
        
        wrong_guess = False 
        if attempt.lower() == "letter" or attempt.lower() == "l":
        
            guess = input(f'Enter your guess: \n').strip()
            while len(guess) == 0 or len(guess) > 1:
                print('Invalid input. Enter a single letter\n')
                guess = input(f'Enter your guess: \n').strip()

            if guess in guessed:
                print('Oops! You already tried that guess, try again!\n')
                continue

            if guess in letters:
                letters.remove(guess)
                keep_searching = True
                while keep_searching:
                    index = words_tuple.index((guess, False))
                    if words_tuple[index][1] == False:
                        words_tuple[index] = (guess, True)
                        keep_searching = False
                
                display = display[:index] + guess + display[index + 1:]
                
            else:
                wrong_guess = True
                
        elif attempt.lower() == "word" or attempt.lower() == "w":
            
            guessed_word = input(f'Enter your guess: \n').strip()
            if guessed_word.lower() == word:
                num_guesses = len(guessed) + 1
                for e in words_tuple:
                    if e[1] == True:
                        num_guesses += 1

                print(f'\nCongrats! You have guessed the word \'{word}\' correctly after {num_guesses} guesses')
                break
            else:
                wrong_guess = True
                guess = guessed_word
            
            
        if wrong_guess:    
                    
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print('   _____ \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 2:
                time.sleep(1)
                print('   _____ \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 3:
                time.sleep(1)
                print('   _____ \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 4:
                time.sleep(1)
                print('   _____ \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |     O \n'
                        '  |      \n'
                        '  |      \n'
                        '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 5:
                time.sleep(1)
                print('   _____ \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |     | \n'
                        '  |     O \n'
                        '  |    /|\ \n'
                        '  |    / \ \n'
                        '__|__\n')
                print('Wrong guess. You\'ve been hanged!!!\n')
                print(f'The word was: {word}')
            
            if count != 5:
                try:
                    with DictionaryApiClient() as client:
                        parser = client.fetch_parser(word)
                    
                    # pick one of the meanings randomly, if there is one at least
                    if len(parser.meanings) > 0:
                        meanings = parser.meanings[0].definitions
                        num_of_meanings = len(meanings)
                        if num_of_meanings > 0:
                            print(f'\nLet me give you a hint...\n')
                            choice = random.randint(0, num_of_meanings - 1)
                            print("It can be a " + parser.meanings[0].part_of_speech)
                            print("Meaning of the word: " + parser.meanings[0].definitions[choice].definition)
                except errors.DictionaryApiNotFoundError:
                    print(f'Ops sorry, no hints available for this word...\n')

        if display == word:
            num_guesses = len(guessed)
            for e in words_tuple:
                if e[1] == True:
                    num_guesses += 1
            print(f'\nCongrats! You have guessed the word \'{word}\' correctly after {num_guesses} guesses')
            break


def play_hangman():
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck!')
    time.sleep(1)
    print('The game is about to start!\nLet\'s play Hangman!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    words_to_guess = [
        'january', 'border', 'image', 'film', 'promise', 'kids',
         'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world'
    ]
    play = True
    while play:
        word = random.choice(words_to_guess)

        hangman(word)
        play = play_again()

    print(f'Thanks for playing, {name}. We expect you back again!')
    exit()


if __name__ == '__main__':
    play_hangman()