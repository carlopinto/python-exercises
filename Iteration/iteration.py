class IterationMethods:

    ### Write a function to count how many odd numbers are in a list.
    def count_odd_numbers(list):
        count = 0
        for e in list:
            if type(e) is int or type(e) is float:
                if e % 2 != 0:
                    count += 1
        return count
    

    ### Sum up all the even numbers in a list.
    def sum_even_numbers(list):
        sum = 0
        for e in list:
            if type(e) is int or type(e) is float:
                if e % 2 == 0:
                    sum += e
        return sum


    ### Sum up all the negative numbers in a list.
    def sum_negative_numbers(list):
        sum = 0
        for e in list:
            if type(e) is int or type(e) is float:
                if e < 0:
                    sum += e
        return sum


    ### Count how many words in a list have length 5
    def count_5letters_words(list):
        count = 0
        for w in list:
            if type(w) is str:
                if len(w) == 5:
                    count += 1
        return count


    ## Sum all the elements in a list up to but not including the first even number. (Write your unit
    # tests. What if there is no even number?)
    def sum_all_except_first_even(list):
        sum = 0
        even_found = False
        for e in list:
            if type(e) is int or type(e) is float:
                if not even_found and e % 2 == 0:
                    even_found = True
                    # print("First even number", e)
                else:
                    sum += e
        return sum


    ### Count how many words occur in a list up to and including the first occurrence of the word
    # “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
    def count_words_upto_sam(list):
        found = False
        count = 0
        for w in list:
            if type(w) is str:
                count += 1
                if w.lower() == "sam":
                    found = True
                    break
        if found:
            return count
        else:
            return 0


    ### Write a function, is_prime, which takes a single integer argument and returns True when the
    # argument is a prime number and False otherwise. Add tests for cases
    def is_prime(n):
        if type(n) is int:
            if n > 1:
                if n == 2:
                    return True
                for i in range(2, n):
                    if n % i == 0:
                        return False
                    else:
                        return True
            else:
                return False
        else:
            return False

    def __init__(self, name):
        self.name = name

    ### Write a function num_even_digits(n) that counts the number of even digits in n.
    def num_even_digits(n):
        """
        Counts the number of even digits in n
        """
        if n == 0:
            return 1
        n = abs(n)
        count = 0
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                count += 1
            n = n // 10
        return count

    ### Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in
    # the list xs.
    def sum_of_squares(xs):
        sum = 0
        for e in xs:
            sum += e ** 2
        return sum
    