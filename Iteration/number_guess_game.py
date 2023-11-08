import random # We cover random numbers in the
rng = random.Random() # modules chapter, so peek ahead.
lb = 1 # lower bound
ub = 1000 # upper bound
number = rng.randrange(lb, ub) # Get random number between [lb and ub).

guesses = 0
msg = ""

while True:
    guess = int(input(msg + "\nGuess my number between {0} and {1}: ".format(lb, ub)))
    guesses += 1
    if guess > number:
        msg += str(guess) + " is too high.\n"
    elif guess < number:
        msg += str(guess) + " is too low.\n"
    else:
        break

print("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))