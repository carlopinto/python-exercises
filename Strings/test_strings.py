import unittest

import string_methods

class TestStringMethods(unittest.TestCase):

    def test_count_letters(self):
        """"""
        self.assertEqual(string_methods.count_letters("banana", "n"), 2)
        self.assertEqual(string_methods.count_letters2("banana", "n"), 2)

        self.assertEqual(string_methods.count_letters2("", "n"), 0)
        self.assertEqual(string_methods.count_letters2("", ""), 1)
        self.assertEqual(string_methods.count_letters2("", " "), 0)

    def test_remove_punctuations(self):
        """"""
        text = "There's no punctuations !in here?"
        self.assertEqual(string_methods.remove_punctuations(text), "Theres no punctuations in here")
    
    def test_reverse_string(self):
        """"""
        text = "reverse"
        self.assertEqual(string_methods.reverse_string(text), "esrever")

    def test_mirror_string(self):
        """"""
        text = "reverse"
        self.assertEqual(string_methods.mirror_string(text), "reverseesrever")   

    def test_remove_occurrences(self):
        """""" 
        text = "reverse"
        self.assertEqual(string_methods.remove_occurrences(text, "e"), "rvrs")

        self.assertEqual(string_methods.remove_occurrences(text, "c"), text)

    def test_is_palindrome(self):
        """"""
        text = "ana"
        self.assertTrue(string_methods.is_palindrome(text))
        text = "hello"
        self.assertFalse(string_methods.is_palindrome(text))

    def test_count(self):
        """"""
        text = "Hello world!"
        self.assertEqual(string_methods.count("lo", text), 1)
        text = "hello"
        self.assertEqual(string_methods.count("l", text), 2)
        text = ""
        self.assertEqual(string_methods.count("l", text), 0)

    def test_remove(self):
        """"""
        text = "Hello world!"
        self.assertEqual(string_methods.remove("lo", text), "Hel world!")
        text = "hello"
        self.assertEqual(string_methods.remove("l", text), "helo")
        text = ""
        self.assertEqual(string_methods.remove("l", text), "")
        self.assertEqual(string_methods.remove("", text), "")

    def test_remove_all(self):
        """"""
        text = "Hello world!"
        self.assertEqual(string_methods.remove_all("lo", text), "Hel world!")
        text = "hello"
        self.assertEqual(string_methods.remove_all("l", text), "heo")
        text = ""
        self.assertEqual(string_methods.remove_all("l", text), "")
        self.assertEqual(string_methods.remove_all("", text), "")
    

if __name__ == '__main__':
    unittest.main()