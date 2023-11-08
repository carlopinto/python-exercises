import unittest

import iteration

class TestIterationMethods(unittest.TestCase):

    def test_count_oddnumbers(self):

        self.assertEqual(iteration.IterationMethods.count_odd_numbers([]), 0)
        self.assertEqual(iteration.IterationMethods.count_odd_numbers([1,2,3,4]), 2)


    def test_sum_evennumbers(self):

        self.assertEqual(iteration.IterationMethods.sum_even_numbers([]), 0)
        self.assertEqual(iteration.IterationMethods.sum_even_numbers([1,2,3,4]), 6)


    def test_sum_negative_numbers(self):

        self.assertEqual(iteration.IterationMethods.sum_negative_numbers([]), 0)
        self.assertEqual(iteration.IterationMethods.sum_negative_numbers([1,-2,3,4]), -2)


    def test_count_5letters_words(self):

        self.assertEqual(iteration.IterationMethods.count_5letters_words([]), 0)
        self.assertEqual(iteration.IterationMethods.count_5letters_words([1,2,3,"hello"]), 1)


    def test_sum_all_except_first_even(self):

        self.assertEqual(iteration.IterationMethods.sum_all_except_first_even([]), 0)
        self.assertEqual(iteration.IterationMethods.sum_all_except_first_even([1,2,3,"hello"]), 4)

    
    def test_count_words_upto_sam(self):

        self.assertEqual(iteration.IterationMethods.count_words_upto_sam([]), 0)
        self.assertEqual(iteration.IterationMethods.count_words_upto_sam([1,2,3,"hello"]), 0)
        self.assertEqual(iteration.IterationMethods.count_words_upto_sam([1,2,3,"sam"]), 1)
        self.assertEqual(iteration.IterationMethods.count_words_upto_sam([1,2,3,"hello","sam"]), 2)


    def test_count_5letters_words(self):

        self.assertEqual(iteration.IterationMethods.count_5letters_words([]), 0)
        self.assertEqual(iteration.IterationMethods.count_5letters_words([1,2,3,"hello"]), 1)


    def test_isprime(self):

        self.assertFalse(iteration.IterationMethods.is_prime(0))
        self.assertFalse(iteration.IterationMethods.is_prime(1))
        self.assertTrue(iteration.IterationMethods.is_prime(2))
        self.assertTrue(iteration.IterationMethods.is_prime(3))
        self.assertFalse(iteration.IterationMethods.is_prime(4))
        self.assertTrue(iteration.IterationMethods.is_prime(15))
        self.assertFalse(iteration.IterationMethods.is_prime(3101988))


    def test_num_even_digits(self):
        """
        """
        self.assertEqual(iteration.IterationMethods.num_even_digits(123456), 3)
        self.assertEqual(iteration.IterationMethods.num_even_digits(2468),4)
        self.assertEqual(iteration.IterationMethods.num_even_digits(1357), 0)
        self.assertEqual(iteration.IterationMethods.num_even_digits(0), 1)
        self.assertEqual(iteration.IterationMethods.num_even_digits(-54690), 3)


    def test_sum_of_squares(self):

        self.assertEqual(iteration.IterationMethods.sum_of_squares([]), 0)
        self.assertEqual(iteration.IterationMethods.sum_of_squares([2,3,4]), 29)
        self.assertEqual(iteration.IterationMethods.sum_of_squares([2,-3,4]), 29)


if __name__ == '__main__':
    unittest.main()