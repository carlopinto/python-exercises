import random
import time

def make_random_ints(num, lower_bound, upper_bound, seeding=0):
    """
    Generate a list containing num random ints between lower_bound
    and upper_bound. upper_bound is an open bound.
    """
    # Create a random number generator
    if seeding != 0:
        # Create generator with known starting state 
        rng = random.Random(seeding) 
    else:
        rng = random.Random()
    result = []
    for _ in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

def make_random_ints_no_dups(num, lower_bound, upper_bound, seeding=0):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """

    # Fix pitfall
    if num > upper_bound - lower_bound:
        return None

    result = []
    if seeding != 0:
        # Create generator with known starting state 
        rng = random.Random(seeding) 
    else:
        rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

def test_time():
    """ Test built-in sum with bespoke sum"""
    sz = 10000000 # Lets have 10 million elements in the list
    testdata = range(sz)

    t0 = time.process_time()
    my_result = do_my_sum(testdata)
    t1 = time.process_time()
    print("my_result = {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))

    t2 = time.process_time()
    their_result = sum(testdata)
    t3 = time.process_time()
    print("their_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))

def cleanword(word):
    import string
    s_clean = ""
    for letter in word:
        if letter not in string.punctuation:
            s_clean += letter
    return s_clean

def has_dashdash(word):
    return "--" in word

def extract_words(word):
    if has_dashdash(word):
        word = " ".join(word.split("--"))
    return cleanword(word).lower().split()

def wordcount(word, l):
    count = 0
    for e in l:
        if word == e:
            count += 1
    return count

def wordset(l):
    l2 = []
    for e in l:
        if e not in l2:
            l2.append(e)
    l2.sort()
    return l2

def longestword(l):
    long = 0
    for e in l:
        if len(e) > long:
            long = len(e)
    return long

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    return new.join(s.split(old))

def test_calendar_module():
    import calendar
    cal = calendar.TextCalendar() # Create an instance
    cal.pryear(2012) # What happens here?

    cal = calendar.TextCalendar(3) # start from Thursday
    cal.pryear(2012) 

    ## Find a function to print just the month in which your birthday occurs this year.
    cal = calendar.TextCalendar() 
    cal.prmonth(2023, 10) 

    d = calendar.LocaleTextCalendar(6, "SPANISH")
    d.pryear(2012)

    print(calendar.isleap(2024))
