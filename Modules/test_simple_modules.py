import unittest

import simple_modules

class TestSimpleModules(unittest.TestCase):

    def test_make_random_ints(self):
        """ It cannot be tested unless we provide a seed"""
        seeding = 5
        self.assertEqual(simple_modules.make_random_ints(5, 1, 10, seeding), [5, 6, 9, 1, 8])

    def test_make_random_ints_no_dups(self):
        """ It cannot be tested unless we provide a seed"""
        seeding = 6
        self.assertEqual(simple_modules.make_random_ints_no_dups(5, 1, 10, seeding), [2, 8, 5, 1, 3])

    def test_make_random_ints_no_dups_pitfall(self):
        """"""
        self.assertEqual(simple_modules.make_random_ints_no_dups(10, 1, 5), None)

    def test_cleanword(self):
        """"""
        self.assertEqual(simple_modules.cleanword("what?"), "what")
        self.assertEqual(simple_modules.cleanword("'now!'"), "now")
        self.assertEqual(simple_modules.cleanword("?+='w-o-r-d!,@$()'"), "word")
        self.assertEqual(simple_modules.cleanword(""), "")

    def test_has_dashdash(self):
        """"""
        self.assertTrue(simple_modules.has_dashdash("distance--but"))
        self.assertFalse(simple_modules.has_dashdash("several"))
        self.assertTrue(simple_modules.has_dashdash("spoke--"))
        self.assertTrue(simple_modules.has_dashdash("distance--but"))
        self.assertFalse(simple_modules.has_dashdash("-yo-yo-"))

    def test_extract_words(self):
        """"""
        self.assertEqual(simple_modules.extract_words("Now is the time! 'Now', is the time? Yes, now."), ['now','is','the','time','now','is','the','time','yes','now'])
        self.assertEqual(simple_modules.extract_words("she tried to curtsey as she spoke--fancy"), ['she','tried','to','curtsey','as','she','spoke','fancy'])

    def test_wordcount(self):
        """"""
        self.assertEqual(simple_modules.wordcount("now", ["now","is","time","is","now","is","is"]), 2)
        self.assertEqual(simple_modules.wordcount("is", ["now","is","time","is","now","the","is"]), 3)
        self.assertEqual(simple_modules.wordcount("time", ["now","is","time","is","now","is","is"]), 1)
        self.assertEqual(simple_modules.wordcount("frog", ["now","is","time","is","now","is","is"]), 0)

    def test_wordset(self):
        """"""
        self.assertEqual(simple_modules.wordset(["now", "is", "time", "is", "now", "is", "is"]), ["is", "now", "time"])
        self.assertEqual(simple_modules.wordset(["I", "a", "a", "is", "a", "is", "I", "am"]), ["I", "a", "am", "is"])
        self.assertEqual(simple_modules.wordset(["or", "a", "am", "is", "are", "be", "but", "am"]), ["a", "am", "are", "be", "but", "is", "or"])

    def test_longestword(self):
        """"""
        self.assertEqual(simple_modules.longestword(["a", "apple", "pear", "grape"]), 5)
        self.assertEqual(simple_modules.longestword(["a", "am", "I", "be"]), 2)
        self.assertEqual(simple_modules.longestword(["this","supercalifragilisticexpialidocious"]), 34)
        self.assertEqual(simple_modules.longestword([ ]), 0)

    def test_myreplace(self):
        """"""
        self.assertEqual(simple_modules.myreplace(",", ";", "this, that, and some other thing"), "this; that; and some other thing")
        self.assertEqual(simple_modules.myreplace(" ", "**", "Words will now be separated by stars."), "Words**will**now**be**separated**by**stars.")
        
        text = "I like to eat"
        self.assertEqual(simple_modules.myreplace("eat", "drink", text), "I like to drink")
        self.assertEqual(simple_modules.myreplace(" ", "-", text), "I-like-to-eat")

        self.assertEqual(simple_modules.myreplace(" ", "-", ""), "")
        self.assertEqual(simple_modules.myreplace(" ", "-", " "), "-")


if __name__ == '__main__':
    unittest.main()