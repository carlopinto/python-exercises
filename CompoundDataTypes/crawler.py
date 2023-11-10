# Crawler crawls the filesystem and builds a dictionary
import os
import json, gzip, io


filecount = 0

def crawl_files(path):
    """ Recursively visit all files in path """
    global filecount

    thedict = {}
    try:
        # Fetch all the entries in the current folder.
        dirlist = os.listdir(path)
        for f in dirlist:
            # Turn each name into full pathname
            fullname = os.path.join(path, f)  

            # If it is a directory, recurse.
            if os.path.isdir(fullname):       
                crawl_files(fullname)
            else:  # Do something useful with the file
                # print("{0:30} {1}".format(f, fullname))
                key = f.lower()  # Normalize the filename
                if key in thedict:
                    thedict[key].append(fullname)
                else:   # insert the key and a list of one pathname
                    thedict[key] = [fullname]

            filecount += 1
            if filecount % 100 == 0:
                print(".", end="")
                if filecount % 5000 == 0:
                    print()
        return thedict
    except FileNotFoundError:
        print("Cannot find the path! Make sure you enter a valid path present on disk.")
        return None

def find_partial_matches(dictionary, key_text):
    partial_matches = {}
    
    for key in dictionary:
        if key_text in key:
            partial_matches[key] = dictionary[key]
    
    return partial_matches

def query(mydict, filename):
    f = filename.lower()
    if f not in mydict:
        print("No hits for '{0}'".format(filename))
        results = find_partial_matches(mydict, f)
        if results == {}:
            print("No partial matches either for '{0}'".format(filename))
        else:
            print("{0} partial matches for '{1}':".format(len(results), filename))
            for (i, result) in enumerate(results):
                print("{0}: {1} is at ".format(i+1, result))
                for p in mydict[result]:
                    print("...", p) 

    else:
        print("{0} is at ".format(filename))
        for p in mydict[f]:
            print("...", p) 

def save_dict(filename, thedict):
    """ Save the dict to disk """
    # f = open(filename, "w")
    f = io.TextIOWrapper(gzip.open(filename, mode="wb"))
    json.dump(thedict, f)
    f.close()

def load_dict(filename):
    """ Load the dict from disk """
    try:
        # f = open(filename, "r")
        f = io.TextIOWrapper(gzip.open(filename, mode="r"))
        mydict = json.load(f)
        f.close()
        print("Loaded {0} filenames for querying.".format(len(mydict)))
        return mydict
    except FileNotFoundError:
        print("The dictionary does not exist on disk yet! Make sure you crawl first.")
        return None

if __name__ == "__main__":

    print("### WELCOME TO THE CRAWLER ###")
    dict_filepath = "CompoundDataTypes/data/mydict.gz"

    while True:
        user_input = input("\nDo you want to crawl or query? ").lower()
        if user_input == "crawl":
            user_filename = input("Enter the path: ")
            the_dict = crawl_files(user_filename)
            if the_dict != None:
                print()
                print("Indexed {0} files, {1} entries in the dictionary.".format(filecount, len(the_dict)))

                save_dict(dict_filepath, the_dict)
                print("The dictionary has been saved.\n")
        elif user_input == "query":

            mydict = load_dict(dict_filepath)
            if mydict != None:
                while True:

                    queryText = input("\nEnter the filename you want to lookup: ")

                    # hit Enter with no text to exit
                    if queryText == "":
                        print("No filename provided! Returning to main menu...")
                        break

                    query(mydict, queryText)
        else:
            print("Wrong command! Exiting...")
            break

