
def add_vectors(list1, list2):
    if list1 is None or list2 is None: return None
    if len(list1) == len(list2):
        list = []
        for (i,v) in enumerate(list1):
            list.append(v + list2[i])
        return list
    else:
        return None

def scalar_mult(s, v):
    if v is None: return None
    list = []
    for e in v:
        list.append(e * s)
    return list

def dot_product(u, v):
    if u is None or v is None: return None
    if len(u) == len(v):
        product = 0
        for (i,value) in enumerate(u):
            product += value * v[i]
        return product
    else:
        return None
    
def cross_product(u, v):
    if u is None or v is None: return None
    if len(u) == len(v) == 3:
        return [(u[1]*v[2])-(u[2]*v[1]), (u[2]*v[0])-(u[0]*v[2]), (u[0]*v[1])-(u[1]*v[0])]
    else:
        return None

def replace(s, old, new):
        if old == "": return s
        l = list(s)
        for (i,v) in enumerate(l):
            a = l[i:i+len(old)]
            if a == list(old):
                l[i:i+len(old)] = list(new)
        return "".join(l)

def swap(x, y): 
    # print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    # print("after swap statement: x:", x, "y:", y)
    return (x, y)

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
    return result

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
    and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

### The word binary means two. Binary search gets its name from the fact that each probe splits the list
### into two pieces and discards the one half from the region of interest.
def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0          # lower bound
    ub = len(xs)    # upper bound
    while True:
        if lb == ub: # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #  .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index # Found it!
        if item_at_mid < target:
            lb = mid_index + 1 # Use upper half of ROI next time
        else:
            ub = mid_index # Use lower half of ROI next time
            
def binary_search_rec(a_list, first, last, an_item):
   if len(a_list) == 0:
       return False
   else:
       mid_point = (first + last) // 2
       if a_list[mid_point] == an_item:
           return True
       else:
           if an_item < a_list[mid_point]:
               last = mid_point - 1
               return binary_search_rec(a_list, first, last, an_item)
           else:
               first = mid_point + 1
               return binary_search_rec(a_list, first, last, an_item)

def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
    duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result

def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs): # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result # And we're done.

        if yi >= len(ys): # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

def merge_v1(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result 
        Return only those items that are present in both lists.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]: # Good, present in both lists
            result.append(ys[yi])
            xi += 1
            yi += 1

        elif xs[xi] < ys[yi]: # Move past this vocab word,
            xi += 1

        else: # Got word that is not in vocab
            yi += 1

def merge_v2(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result 
        Return only those items that are present in the first list, but not in the second.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]: # move on
            xi += 1
            yi += 1

        elif xs[xi] < ys[yi]: # Good, present in first list in second
            result.append(xs[xi])
            xi += 1

        else: # move on in second list
            yi += 1

# or merge_v3
def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
    list of words from wds that do not occur in vocab.
    Return only those items that are present in the second list, but not in the first.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]: # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]: # Move past this vocab word,
            xi += 1

        else: # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1

def merge_v4(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result 
        Return items that are present in either the first or the second list.
    """
    result = []
    xi = 0
    yi = 0
    previous = None

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result
        
        if  xs[xi] == previous:
            xi +=1

        if  ys[yi] == previous:
            yi +=1

        if xs[xi] == ys[yi]: # move on
            result.append(xs[xi])
            previous = xs[xi]
            xi += 1
            yi += 1

        elif xs[xi] < ys[yi]: # Good, present in first list in second
            result.append(xs[xi])
            previous = xs[xi]
            xi += 1

        else: # move on in second list
            result.append(ys[yi])
            previous = ys[yi]
            yi += 1

def merge_v5(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result 
        Return items from the first list that are not eliminated 
        by a matching element in the second list.
    """
    result = []
    xi = 0
    yi = 0

    while(True):
        if yi >= len(ys):
            if len(xs) > 0 and xi < len(xs):
                result.append(xs[xi])
                yi = 0
                xi += 1
        
        if xi >= len(xs):
            return result
        
        if xs[xi] == ys[yi]:
            ys = ys[:yi] + ys[yi+1:]
            xi += 1
        else:
            yi += 1

def sort_list_of_letters(words_list):
    """ 
        Returns a list of words in alphabetical order which occur in the 
        given list together with the number of times each word occurs
    """
    words = {}
    for word in words_list:
        if word != " ":
            words[word] = words.get(word, 0) + 1

    # use a list to sort in alphabetical order
    word_items = list(words.items())
    word_items.sort()

    return words, word_items

def write_words_to_file(words, filename):
    """ Write words to file """
    f = open(filename, "w")
    for (word,n) in words:
        f.write(word + " " + str(n) + " ")
    f.close()

def get_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest