### Every week a computer scientist buys four lotto tickets. She always chooses 
### the same prime numbers, with the hope that if she ever hits the jackpot, she 
### will be able to go onto TV and Facebook and tell everyone her secret. This will 
### suddenly create widespread public interest in prime numbers, and will be the 
### trigger event that ushers in a new age of enlightenment.

import random

# Each lotto draw takes six random balls, numbered from 1 to 49. Write a function to return a lotto draw.
def lotto_draw():
    return make_random_ints_no_dups(6, 1, 50)

# from Modules/simple_modules.py
def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """

    # Fix pitfall
    if num > upper_bound - lower_bound:
        return None

    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

# Write a function that compares a single ticket and a draw, and returns the number of correct picks on that ticket
def lotto_match(ticket, draw):
    ticket.sort()
    draw.sort()

    from vectors_methods import merge_v1

    l = merge_v1(ticket, draw)

    return len(l)

# Write a function that takes a list of tickets and a draw, and returns a list telling how many picks were correct on each ticket
def lotto_matches(draw, tickets):
    correct = []
    for t in tickets:
        correct.append(lotto_match(t, draw))

    return correct

def is_prime(n):
        if type(n) is int:
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        return False
                return True
            else:
                return False
        else:
            return False

# Write a function that takes a list of integers, and returns the number of primes in the list
def primes_in(draw):
    primes = 0
    for d in draw:
        if is_prime(d):
            primes += 1
    
    return primes

def list_primes(up_to):
    primes = []
    for i in range(1, up_to):
        if is_prime(i):
            primes.append(i)
    return primes

def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list

# Write a function to discover whether the computer scientist has missed any prime numbers 
# in her selection of the four tickets. Return a list of all primes that she has missed
def prime_misses(tickets):
    tickets = flatten_concatenation(my_tickets)
    tickets.sort()
    from vectors_methods import find_unknowns_merge_pattern
    return find_unknowns_merge_pattern(tickets, list_primes(50))

# Write a function that repeatedly makes a new draw, and compares the draw to the four tickets.
def repeat(tickets, corrects):
    count = 0
    while(True):
        draw = lotto_draw()
        matches = lotto_matches(draw, tickets)
        if corrects in matches:
            break
        else:
            count += 1
    
    print("{0} correct picks after {1} draws.".format(corrects, count))


my_tickets = [  [ 7, 17, 37, 19, 23, 43],
                [ 7, 2, 13, 41, 31, 43],
                [ 2, 5, 7, 11, 13, 17],
                [13, 17, 37, 19, 23, 43] ]

# print(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
# print(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

# print(primes_in([42, 4, 7, 11, 1, 13]) == 3)
# print(prime_misses(my_tickets) == [3, 29, 47])

repeat(my_tickets, 5) # ~ 4 million draws for 6 correct picks