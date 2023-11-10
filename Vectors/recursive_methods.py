### To sum all the numbers in our recursive nested number list we need to:
### traverse the list, 
### visiting each of the elements within its nested structure, 
### adding any numeric elements to our sum, 
### and recursively repeating the summing process with any elements which are themselves sub-lists

import os

def recursive_sum(nested_num_list):
    """ Sum all the numbers in our recursive nested number list """
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += recursive_sum(element)
        else:
            try:
                tot += element
            except TypeError:
                print("'{0}' is not a valid type".format(element))
    return tot

def recursive_max(nxs):
    """ 
      Find the maximum in a recursive structure of lists 
      within other lists.
    """
    if len(nxs) == 0: return None
    largest = None 
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            if len(e) > 0:
                val = recursive_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

def recursive_min(nxs):
    """ 
      Find the minimum in a recursive structure of lists 
      within other lists.
    """
    if len(nxs) == 0: return None
    smallest = None 
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            if len(e) > 0:
                val = recursive_min(e)
        else:
            val = e

        if first_time or val < smallest:
            smallest = val
            first_time = False

    return smallest

def count(number, nxs):
    """ 
      Returns the number of occurrences of target in a nested list 
    """
    occurrences = 0
    for e in nxs:
        if type(e) == type([]):
            occurrences += count(number, e)
        else:
            if e == number:
                occurrences += 1

    return occurrences

def flatten(nxs):
    """ 
      Returns a simple list containing all the values in a nested list
    """
    flat = []
    for e in nxs:
        if type(e) == type([]):
            flat.extend(flatten(e))
        else:
            flat.append(e)

    return flat

def get_dirlist(path):
    """ 
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line 
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse. 
            print_files(fullname, prefix + "| ")

# Use the commented code in the function below to
#   Write a program that creates an empty file named trash.txt in each subdirectory 
#   of a directory tree given the root of the tree as an argument (or the current directory as a default). 
#   Now write a program that removes all these files.

def list_files(path):
    """ 
        Return a list of all the full paths of files in the directory or the subdirectories. 
        (Do not include directories in this list — just files)    
    """
    files = []
    # f = open(os.path.join(path, "trash.txt"),"w")
    # f.close()
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)   # Turn name into full pathname
        
        if os.path.isdir(fullname):        # If a directory, recurse. 
            files.extend(list_files(fullname))
        else:
            files.append(os.path.abspath(fullname))
            # if f == "trash.txt":
            #     os.remove(fullname)
            #     print("Trash found! {0}".format(fullname))

    return files

if __name__ == "__main__":
    print_files("Vectors")
    print(len(list_files("Vectors")))