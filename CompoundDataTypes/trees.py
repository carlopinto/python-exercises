
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)
    
    def to_dict(self):
        """
        Convert the tree to a dictionary representation.
        """
        tree_dict = {
            'cargo': self.cargo,
        }
        if self.left:
            tree_dict['left'] = self.left.to_dict()
        if self.right:
            tree_dict['right'] = self.right.to_dict()
        return tree_dict
    
    def from_dict(self, tree_dict):
        """
        Create a Tree object from a dictionary representation.
        """
        cargo = tree_dict['cargo']
        left = tree_dict.get('left')
        right = tree_dict.get('right')
        left_tree = self.from_dict(left) if left else None
        right_tree = self.from_dict(right) if right else None
        return Tree(cargo, left_tree, right_tree)
    
def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")

def print_tree_inorder(tree):
    if tree is None: return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

def get_token(token_list, expected):
    """ 
    Takes a token list and an expected token as parameters. 
    It compares the expected token to the first token on the list: 
    if they match, it removes the token from the list and returns True; 
    otherwise, it returns False
    """
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    """
    Handles operands. If the next token in token_list is a number, 
    get_number removes it and returns a leaf node containing the number; 
    otherwise, it returns None
    """
    if get_token(token_list, "("):
        x = get_sum(token_list)         # Get the subexpression
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis") 
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    """ Builds an expression tree for products """
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return Tree("*", a, b)
    return a

def get_sum(token_list):
    """
    Tries to build a tree with a product on the left and 
    a sum on the right. But if it doesn’t find a +, it just builds a product
    """
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a

# token_list = [9, "*", 11, "end"]
# tree = get_product(token_list)
# print_tree_postorder(tree)

# token_list = [9, "+", 11, "end"]
# tree = get_product(token_list)
# print_tree_postorder(tree)

# token_list = [2, "*", 3, "*", 5 , "*", 7, "end"]
# tree = get_product(token_list)
# print_tree_postorder(tree)

# token_list = [9, "*", 11, "+", 5 , "*", 7, "end"]
# tree = get_sum(token_list)
# print_tree_postorder(tree)

# token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
# tree = get_sum(token_list)
# print_tree_postorder(tree)

import json

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    root = Tree("bird")

    # Read knowledge tree from file - if it exists
    try:
        with open("CompoundDataTypes/data/animals.json", 'r') as file:
            filecontent = file.read()
            deserialized_tree_dict  = json.loads(filecontent)
            root = root.from_dict(deserialized_tree_dict)
            print("Tree loaded from JSON file.")
    except FileNotFoundError:
        print("The file 'animals.json' does not exist.")

    # print_tree_indented(root)

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
    
    # Save knowledge to file
    tree_dict = root.to_dict()
    serialized_tree = json.dumps(tree_dict)

    with open("CompoundDataTypes/data/animals.json", 'w') as file:
        file.write(serialized_tree)
        print("Tree saved to file as JSON.")

if __name__ == "__main__":
    animal()