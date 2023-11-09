
def count_letters(s, l):
    """ Traverse the string """
    count = 0
    for c in s:
        if c == l:
            count += 1
    return count

def count_letters2(s, l, all=True):
    """ Call find instead of traversing the string """
    start_index = 0
    count = 0
    while(s.find(l, start_index) != -1):
        count += 1
        if not all:
            return count
        start_index = s.find(l, start_index) + 1
            
    return count

def remove_punctuations(s):
    import string
    s_clean = ""
    for letter in s:
        if letter not in string.punctuation:
            s_clean += letter
    return s_clean

def parse_text(s, l, case_sensitive=True):

    words = remove_punctuations(s).split()
    total_words = len(words)
    num_words = 0
    for word in words:
        if not case_sensitive:
            if l.lower() in word.lower():
                num_words += 1
            else:
                if l in word:
                    num_words += 1
    
    perc = num_words / total_words * 100

    print("Your text contains {0} words, of which {1} ({2}%) contain a '{3}'".format(total_words, num_words, perc, l))

### Print a neat looking multiplication table
def print_multiples(n, high):
    for i in range(1, high+1):
        if n == 0:
            if i == 1:
                print("", end="\t")
            elif i == high:
                print(i-1, end="\t")
                print(i, end="\t")
            else:
                print(i-1, end="\t")
        else:
            if i == 1:
                print(str(n) + ":", end="\t")
            
            print(n * i, end="\t")
    print()

    if n == 0:
        for i in range(1, high+1):
            if i == 1:
                print(" :------", end="")
            elif i == high:
                print("----------", end="")
                print("-----------", end="")
            else:
                print("-------", end="")
        print()

def print_mult_table(high):
    for i in range(0, high+1):
        print_multiples(i, high)

### Write a function that reverses its string argument
def reverse_string(s):
    reversed_string = ""
    index = len(s) - 1
    while(index >= 0):
        reversed_string += s[index]
        index -= 1

    return reversed_string

def mirror_string(s):
    return s + reverse_string(s)

### Write a function that removes all occurrences of a given letter from a string:
def remove_occurrences(s, l):
    clear_string = ""
    for e in s:
        if e != l:
            clear_string += e
    return clear_string

### Write a function that recognizes palindromes.
def is_palindrome(s):
    return s == reverse_string(s)

### Write a function that counts how many times a substring occurs in a string
def count(w, s):
    c = 0
    for e in range(0, len(s) - len(w) + 1):
        substr = ""
        for a in range(e, e + len(w)):
            substr += s[a]
        if substr == w:
            c += 1
    return c

### Write a function that removes the first occurrence of a string from another string
def remove(w, s):
    new_str = s
    for e in range(0, len(s) - len(w) + 1):
        substr = ""
        for a in range(e, e + len(w)):
            substr += s[a]
        if substr == w:
            new_str = s[:e]
            new_str += s[e+len(w):]
    return new_str

### Write a function that removes the first occurrence of a string from another string
def remove_all(w, s):
    if w == "": return "" # prevents endless loop
    while(w in s):
        s = remove(w, s)
    return s