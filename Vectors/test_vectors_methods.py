import unittest

import vectors_methods

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


if __name__ == '__main__':
    unittest.main()