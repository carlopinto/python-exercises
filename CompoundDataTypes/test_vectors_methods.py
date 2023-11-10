import unittest

import vectors_methods, recursive_methods

class TestVectorsMethods(unittest.TestCase):

    def test_add_vectors(self):
        """"""
        self.assertEqual(vectors_methods.add_vectors([1, 2, 3], [2, 3, 4]), [3, 5, 7])
        self.assertEqual(vectors_methods.add_vectors([0, 0, 0], [0, 0, 0]), [0, 0, 0])

    def test_add_vectors_different_lenghts(self):
        """"""
        self.assertEqual(vectors_methods.add_vectors([1, 2, 3], [2, 3]), None)
        self.assertEqual(vectors_methods.add_vectors([1, 2, 3], []), None)
        self.assertEqual(vectors_methods.add_vectors([1, 2, 3], None), None)

    def test_scalar_mult(self):
        """"""
        self.assertEqual(vectors_methods.scalar_mult(2, [2, 3, 4]), [4, 6, 8])
        self.assertEqual(vectors_methods.scalar_mult(0, [1, 2, 3]), [0, 0, 0])

        self.assertEqual(vectors_methods.scalar_mult(0, []), [])
        self.assertEqual(vectors_methods.scalar_mult(0, None), None)

    def test_dot_product(self):
        """"""
        self.assertEqual(vectors_methods.dot_product([1, 2, 3], [2, 3, 4]), 20)
        self.assertEqual(vectors_methods.dot_product([1, 2, 3], [1, 2, 3]), 14)
        self.assertEqual(vectors_methods.dot_product([0, 1, 0], [1, 2, 3]), 2)
        self.assertEqual(vectors_methods.dot_product([0, 0, 0], [1, 2, 3]), 0)

        self.assertEqual(vectors_methods.dot_product([], []), 0)
        self.assertEqual(vectors_methods.dot_product([1, 2, 3], []), None)
        self.assertEqual(vectors_methods.dot_product([], None), None)

    def test_cross_product(self):
        """"""
        self.assertEqual(vectors_methods.cross_product([1, 2, 3], [2, 3, 4]), [-1, 2, -1])
        self.assertEqual(vectors_methods.cross_product([1, 2, 3], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(vectors_methods.cross_product([0, 1, 0], [1, 2, 3]), [3, 0, -1])
        self.assertEqual(vectors_methods.cross_product([0, 0, 0], [1, 2, 3]), [0, 0, 0])

        self.assertEqual(vectors_methods.cross_product([], []), None)
        self.assertEqual(vectors_methods.cross_product([1, 2, 3], []), None)
        self.assertEqual(vectors_methods.cross_product([], None), None)

    def test_replace(self):
        """"""
        text = "I like to eat"
        self.assertEqual(vectors_methods.replace(text, "eat", "drink"), "I like to drink")
        self.assertEqual(vectors_methods.replace(text, " ", "-"), "I-like-to-eat")

        self.assertEqual(vectors_methods.replace("", "", "-"), "")
        self.assertEqual(vectors_methods.replace("", " ", "-"), "")
        self.assertEqual(vectors_methods.replace(" ", "", "-"), " ")
        self.assertEqual(vectors_methods.replace(" ", " ", "-"), "-")

    def test_swap(self):
        """"""
        a = ["This", "is", "fun"]
        b = [2,3,4]
        # assign the return value from swap to (a, b)
        a, b = vectors_methods.swap(a, b)
        self.assertEqual(b, ["This", "is", "fun"])
        self.assertEqual(a, [2,3,4])

    def test_swap_wrong(self):
        """"""
        a = ["This", "is", "fun"]
        b = [2,3,4]
        vectors_methods.swap(a, b)

        # check that swap did not update a and b
        self.assertEqual(a, ["This", "is", "fun"])
        self.assertEqual(b, [2,3,4])
        self.assertNotEqual(b, ["This", "is", "fun"])
        self.assertNotEqual(a, [2,3,4])

    def test_search_linear(self):
        """"""
        sz = 10000000 # Lets have 10 million elements in the list
        xs = range(sz)
        self.assertEqual(vectors_methods.search_linear(xs, 9999999), 9999999)
        self.assertEqual(vectors_methods.search_linear(xs, 99999999), -1)

    def test_find_unknown_words(self):
        """"""
        vocab = ["apple", "boy", "dog", "down", 
                          "fell", "girl", "grass", "the", "tree"]
        book_words = "the apple fell from the tree to the grass".split()
        self.assertEqual(vectors_methods.find_unknown_words(vocab, book_words), ["from", "to"])
        self.assertEqual(vectors_methods.find_unknown_words([], book_words), book_words)
        self.assertEqual(vectors_methods.find_unknown_words(vocab, ["the", "boy", "fell"]), [])

    def test_text_to_words(self):
        """"""
        words = "the apple fell from the tree to the grass"
        self.assertEqual(vectors_methods.text_to_words(words), ["the", "apple", "fell", "from", "the", "tree", "to", "the", "grass"])

        self.assertEqual(vectors_methods.text_to_words(""), [])
        self.assertEqual(vectors_methods.text_to_words(" "), [])
        self.assertEqual(vectors_methods.text_to_words("hello"), ["hello"])

    def test_get_words_in_book(self):
        """"""
        book_words = vectors_methods.get_words_in_book("CompoundDataTypes/alice_in_wonderland.txt")
        self.assertEqual(len(book_words), 27336)

    def test_load_words_from_file(self):
        """"""
        book_words = vectors_methods.load_words_from_file("CompoundDataTypes/alice_in_wonderland.txt")
        self.assertEqual(len(book_words), 26443)
        
    def test_search_binary(self):
        """"""
        sz = 10000000 # Lets have 10 million elements in the list
        xs = range(sz)
        self.assertEqual(vectors_methods.search_linear(xs, 9999999), 9999999)
        self.assertEqual(vectors_methods.search_linear(xs, 99999999), -1)

    def test_remove_adjacent_dups(self):
        """"""
        all_words = vectors_methods.get_words_in_book("CompoundDataTypes/alice_in_wonderland.txt")
        all_words.sort()
        book_words = vectors_methods.remove_adjacent_dups(all_words)
        # All words
        self.assertEqual(len(all_words), 27336)
        # Unique words
        self.assertEqual(len(book_words), 2569)

    def test_merge(self):
        """"""
        xs = [1,3,5,7,9,11,13,15,17,19,20,24]
        ys = [3,4,8,12,16,20,24]
        self.assertEqual(vectors_methods.merge(xs, ys), [1, 3, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 20, 24, 24])

    def test_merge_v1(self):
        """"""
        xs = [1,3,5,7,9,11,13,15,17,19,20,24]
        ys = [3,4,8,12,16,20,24]
        self.assertEqual(vectors_methods.merge_v1(xs, ys), [3, 20, 24])

    def test_merge_v2(self):
        """"""
        xs = [1,3,5,7,9,11,13,15,17,19,20,24]
        ys = [3,4,8,12,16,20,24]
        self.assertEqual(vectors_methods.merge_v2(xs, ys), [1, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_find_unknowns_merge_pattern(self):
        """"""
        xs = [1,3,5,7,9,11,13,15,17,19,20,24]
        ys = [3,4,8,12,16,20,24]
        self.assertEqual(vectors_methods.find_unknowns_merge_pattern(xs, ys), [4, 8, 12, 16])

    def test_merge_v4(self):
        """"""
        xs = [1,3,5,7,9,11,13,15,17,19,20,24]
        ys = [3,4,8,12,16,20,24]
        self.assertEqual(vectors_methods.merge_v4(xs, ys), [1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 24])

    def test_merge_v5(self):
        """ an item in the second list “knocks out” just one matching item in the first list """
        
        xs5 = [5,7,11,11,11,12,13]
        ys5 = [7,8,11]
        self.assertEqual(vectors_methods.merge_v5(xs5, ys5), [5, 11, 11, 12, 13])

        xs = [1,3,5,7,9,11,13,15,17,19,20,24]
        ys = [3,4,8,12,16,20,24]
        self.assertEqual(vectors_methods.merge_v5(xs, ys), [1, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_load_sort_write_words_to_file(self):
        """ 
            Creates a text file named alice_words.txt containing an alphabetical listing of all the words, 
            and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland.
        """
        words = vectors_methods.get_words_in_book("CompoundDataTypes/alice_in_wonderland.txt")
        words_dict, sorted_words = vectors_methods.sort_list_of_letters(words)
        vectors_methods.write_words_to_file(sorted_words, "CompoundDataTypes/alice_words.txt")

        print("The word 'Alice' occurs {0} times in the book.".format(words_dict["alice"]))
        longest_word = vectors_methods.get_longest_word(words_dict.keys())
        print("The longest word in the book is '{0}' and it has {1} characters".format(longest_word, len(longest_word)))

class TestRecursiveMethods(unittest.TestCase):

    def test_recursive_sum(self):
        """"""
        self.assertEqual(recursive_methods.recursive_sum([1, 2, [11, 13], 8]), 35)
        self.assertEqual(recursive_methods.recursive_sum([]), 0)
        self.assertEqual(recursive_methods.recursive_sum(["test"]), 0)

    def test_recursive_max(self):
        """"""
        self.assertEqual(recursive_methods.recursive_max([1, 2, [11, 13], 8]), 13)
        self.assertEqual(recursive_methods.recursive_max([]), None)
        self.assertEqual(recursive_methods.recursive_max([1, 2, []]), 2)
        self.assertEqual(recursive_methods.recursive_max(["test"]), "test")
        self.assertEqual(recursive_methods.recursive_max([""]), "")

    def test_recursive_min(self):
        """"""
        self.assertEqual(recursive_methods.recursive_min([1, 2, [11, 13], 8]), 1)
        self.assertEqual(recursive_methods.recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]), -13)
        self.assertEqual(recursive_methods.recursive_min([]), None)
        self.assertEqual(recursive_methods.recursive_min([1, 2, []]), 1)
        self.assertEqual(recursive_methods.recursive_min(["test"]), "test")
        self.assertEqual(recursive_methods.recursive_min([""]), "")

    def test_count(self):
        """"""
        self.assertEqual(recursive_methods.count(2, []), 0)
        self.assertEqual(recursive_methods.count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]), 4)
        self.assertEqual(recursive_methods.count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]), 2)
        self.assertEqual(recursive_methods.count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]), 0)
        self.assertEqual(recursive_methods.count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]), 6)
        self.assertEqual(recursive_methods.count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]), 4)

    def test_flatten(self):
        """"""
        self.assertEqual(recursive_methods.flatten([2,9,[2,1,13,2],8,[2,6]]), [2,9,2,1,13,2,8,2,6])
        self.assertEqual(recursive_methods.flatten([[9,[7,1,13,2],8],[7,6]]), [9,7,1,13,2,8,7,6])
        self.assertEqual(recursive_methods.flatten([[9,[7,1,13,2],8],[2,6]]), [9,7,1,13,2,8,2,6])
        self.assertEqual(recursive_methods.flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]),
                                                       ["this","a","thing","a","is","a","easy"])
        self.assertEqual(recursive_methods.flatten([]), [])


if __name__ == '__main__':
    unittest.main()