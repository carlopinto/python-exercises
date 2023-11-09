### From Vectors module, add two changes.
### At the top of that program, we import the module that we’ve been working on here 
### (assume we called it draw_queens). (You’ll have to ensure that the two modules are 
### saved in the same folder.) Then after line 10 here we add a call to draw the solution 
### that we’ve just discovered:
###     draw_queens.draw_board(bd)
### And that gives a very satisfying combination of program that can search for solutions 
### to the N queens problem, and when it finds each, it pops up the board showing the solution

import draw_queens

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0) # Calc the absolute y distance
    dx = abs(x1 - x0) # CXalc the absolute x distance
    return dx == dy # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
    with any queen to its left.
    """
    for i in range(c): # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
    We're assuming here that the_board is a permutation of column
    numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

# Begin with the permutation [0,1,2,3,4,5,6,7] and we’ll repeatedly shuffle the list, 
# and test each to see if it works! Along the way we’ll count how many attempts we 
# need before we find each solution, and we’ll find 10 solutions

def main():
    import random
    rng = random.Random() # Instantiate a generator
    solutions = []
    count = 0
    bd = list(range(8)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd not in solutions:
                print("Found solution {0} in {1} tries.".format(bd, tries))
                draw_queens.draw_board(bd)
                tries = 0
                num_found += 1
                solutions.append(bd[:])
                print("Found mirror solution {0}".format(mirror_solution_X(bd)))
                
            else:
                count += 1
            
    print("Found similar solution {0} times".format(count))


def mirror_solution_Y(bd):
    mirror = []
    for e in bd:
        mirror.append(len(bd) - 1 - e)

    return mirror

def mirror_solution_X(bd):
    mirror = bd[:]
    mirror.reverse()
    return mirror

b = [0,4,7,5,2,6,1,3]

def rotate_matrix( m ):
    new_matrix = []
    for i in range(len(m[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], m)))

    return new_matrix

def from_list_to_matrix(l):
    matrix = [[0 for col in range(len(l))] for row in range(len(l))]
    for i in range(len(l)):
        matrix[l[i]][i] = 1

    return matrix

def from_matrix_to_list(m):
    l = []
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if m[j][i] == 1:
                l.append(j)

    return l

def generate_family_symmetries(bd):
    family = []
    family.append(bd)
    family.append(mirror_solution_Y(mirror_solution_X(bd))) # equals to rotate by 180
    family.append(mirror_solution_X(bd))
    family.append(mirror_solution_Y(bd))
    # rotate 90 degrees anti-clockwise
    m2 = rotate_matrix(from_list_to_matrix(b))
    family.append(from_matrix_to_list(m2))
    # rotate 270 degrees anti-clockwise
    l4 = from_matrix_to_list(rotate_matrix(rotate_matrix(m2)))
    family.append(l4)
    family.append(mirror_solution_X(l4))
    family.append(mirror_solution_Y(l4))

    return family

# Change main() to only print solutions from unique families.

def main2():
    import random
    rng = random.Random() # Instantiate a generator
    solutions = []
    count = 0
    family_count = 0
    bd = list(range(8)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd not in solutions:

                # only solutions from unique families
                family_found = False
                family = generate_family_symmetries(bd)
                for sol in solutions:
                    if sol in family:
                        family_found = True
                        break
                family = []
                if family_found:
                    family_count += 1
                else:
                    print("{2}: Found solution {0} in {1} tries.".format(bd, tries, num_found+1))
                    draw_queens.draw_board(bd, num_found)
                    tries = 0
                    num_found += 1
                    solutions.append(bd[:])
            else:
                count += 1
            
    print("Found similar solution {0} times".format(count))
    print("Found family solution {0} times".format(family_count))

if __name__ == "__main__":
    import time
    t0 = time.process_time()
    main2()
    t1 = time.process_time()
    print("That took {0:.4f} seconds.".format(t1-t0))