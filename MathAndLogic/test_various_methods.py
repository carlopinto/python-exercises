import unittest

import various_methods

class TestMathsMethods(unittest.TestCase):

    def test_abs_positive(self):
        """
        Test the absolute value
        """
        self.assertEqual(various_methods.BespokeMethods.absolute_value(17), 17)

    def test_abs_negative(self):
        """
        Test the absolute value
        """
        self.assertEqual(various_methods.BespokeMethods.absolute_value(-17), 17)

    def test_abs_zero(self):
        """
        Test the absolute value
        """
        self.assertEqual(various_methods.BespokeMethods.absolute_value(0), 0)

    def test_abs_float(self):
        """
        Test the absolute value
        """
        self.assertEqual(various_methods.BespokeMethods.absolute_value(3.14), 3.14)

    def test_maths(self):
        """
        Test - math operations
        """
        self.assertEqual(various_methods.BespokeMethods.hypotenuse(3,4), 5)
        self.assertEqual(various_methods.BespokeMethods.hypotenuse(12, 5), 13.0)
        self.assertEqual(various_methods.BespokeMethods.hypotenuse(24, 7), 25.0)
        self.assertEqual(various_methods.BespokeMethods.hypotenuse(9, 12), 15.0)

        self.assertEqual(various_methods.BespokeMethods.slope(5, 3, 4, 2), 1.0)
        self.assertEqual(various_methods.BespokeMethods.slope(1, 2, 3, 2), 0.0)
        self.assertEqual(various_methods.BespokeMethods.slope(1, 2, 3, 3), 0.5)
        self.assertEqual(various_methods.BespokeMethods.slope(2, 4, 1, 2), 2.0)

        self.assertEqual(various_methods.BespokeMethods.intercept(1, 6, 3, 12), 3.0)
        self.assertEqual(various_methods.BespokeMethods.intercept(6, 1, 1, 6), 7.0)
        self.assertEqual(various_methods.BespokeMethods.intercept(4, 6, 12, 8), 5.0)

        self.assertTrue(various_methods.BespokeMethods.is_even(2))
        self.assertFalse(various_methods.BespokeMethods.is_even(3))
        self.assertEqual(various_methods.BespokeMethods.is_even("bambino"), None)
        self.assertFalse(various_methods.BespokeMethods.is_odd(2))
        self.assertTrue(various_methods.BespokeMethods.is_odd(3))
        self.assertEqual(various_methods.BespokeMethods.is_odd("bambino"), None)

        self.assertTrue(various_methods.BespokeMethods.is_factor(3, 12))
        self.assertTrue(not various_methods.BespokeMethods.is_factor(5, 12))
        self.assertTrue(various_methods.BespokeMethods.is_factor(7, 14))
        self.assertTrue(not various_methods.BespokeMethods.is_factor(7, 15))
        self.assertTrue(various_methods.BespokeMethods.is_factor(1, 15))
        self.assertTrue(various_methods.BespokeMethods.is_factor(15, 15))
        self.assertTrue(not various_methods.BespokeMethods.is_factor(25, 15))

        self.assertTrue(various_methods.BespokeMethods.is_multiple(12, 3))
        self.assertTrue(various_methods.BespokeMethods.is_multiple(12, 4))
        self.assertTrue(not various_methods.BespokeMethods.is_multiple(12, 5))
        self.assertTrue(various_methods.BespokeMethods.is_multiple(12, 6))
        self.assertTrue(not various_methods.BespokeMethods.is_multiple(12, 7))

    def test_mysum(self):
        """
        Test - sum all the elements in a list
        """
        self.assertEqual(various_methods.BespokeMethods.sum_list_elements([1, 2, 3, 4]), 10)
        self.assertEqual(various_methods.BespokeMethods.sum_list_elements([1.25, 2.5, 1.75]), 5.5)
        self.assertEqual(various_methods.BespokeMethods.sum_list_elements([1, -2, 3]), 2)
        self.assertEqual(various_methods.BespokeMethods.sum_list_elements([ ]), 0)
        self.assertEqual(various_methods.BespokeMethods.sum_list_elements(range(11)), 55) # 11 is not included in the list

class TestLogicMethods(unittest.TestCase):

    def test_turnclockwise(self):
        """
        Test turn clockwise
        """
        self.assertEqual(various_methods.BespokeMethods.turn_clockwise("N"), "E")

    def test_turnclockwise_edge(self):
        """
        Test turn clockwise
        """
        self.assertEqual(various_methods.BespokeMethods.turn_clockwise("W"), "N")

    def test_turnclockwise_int(self):
        """
        Test turn clockwise
        """
        self.assertEqual(various_methods.BespokeMethods.turn_clockwise(42), None)

    def test_turnclockwise_str(self):
        """
        Test turn clockwise
        """
        self.assertEqual(various_methods.BespokeMethods.turn_clockwise("ciaobella"), None)

    def test_dayname(self):
        """
        Test day name
        """
        self.assertEqual(various_methods.BespokeMethods.day_name(3), "Wednesday")
        self.assertEqual(various_methods.BespokeMethods.day_name(6), "Saturday")
        self.assertEqual(various_methods.BespokeMethods.day_name(50), None)

    def test_daynum(self):
        """
        Test day number
        """
        self.assertEqual(various_methods.BespokeMethods.day_num("Friday"), 5)
        self.assertEqual(various_methods.BespokeMethods.day_num("Sunday"), 0)
        self.assertEqual(various_methods.BespokeMethods.day_num(various_methods.BespokeMethods.day_name(3)), 3)
        self.assertEqual(various_methods.BespokeMethods.day_name(various_methods.BespokeMethods.day_num("Thursday")), "Thursday")
        self.assertEqual(various_methods.BespokeMethods.day_num("Halloween"), None)

    def test_dayadd(self):
        """
        Test day add
        """
        self.assertEqual(various_methods.BespokeMethods.day_add("Sunday", 5), "Friday")
        self.assertEqual(various_methods.BespokeMethods.day_add("Tuesday", 0), "Tuesday")
        self.assertEqual(various_methods.BespokeMethods.day_add("Tuesday", 14), "Tuesday")
        self.assertEqual(various_methods.BespokeMethods.day_add("Sunday", 100), "Tuesday")
        self.assertEqual(various_methods.BespokeMethods.day_add("Sunday", -1), "Saturday")
        self.assertEqual(various_methods.BespokeMethods.day_add("Sunday", -7), "Sunday")
        self.assertEqual(various_methods.BespokeMethods.day_add("Tuesday", -100), "Sunday")

    def test_daysinmonth(self):
        """
        Test day in month
        """
        self.assertEqual(various_methods.BespokeMethods.days_in_month("February"), 28)
        self.assertEqual(various_methods.BespokeMethods.days_in_month("December"), 31)
        self.assertEqual(various_methods.BespokeMethods.days_in_month("Carlo"), None)
    
    def test_tosecs(self):
        """
        Test to seconds
        """
        self.assertEqual(various_methods.BespokeMethods.to_secs(2, 30, 10), 9010)
        self.assertEqual(various_methods.BespokeMethods.to_secs(2, 0, 0), 7200)
        self.assertEqual(various_methods.BespokeMethods.to_secs(0, 2, 0), 120)
        self.assertEqual(various_methods.BespokeMethods.to_secs(0, 0, 42), 42)
        self.assertEqual(various_methods.BespokeMethods.to_secs(0, -10, 10), -590)
        self.assertEqual(various_methods.BespokeMethods.to_secs(2.5, 0, 10.71), 9010)
        self.assertEqual(various_methods.BespokeMethods.to_secs(2.433, 0, 0), 8758)

    def test_fromseconds(self):
        """
        Test from seconds
        """
        self.assertEqual(various_methods.BespokeMethods.hours_in(9010), 2)
        self.assertEqual(various_methods.BespokeMethods.minutes_in(9010), 30)
        self.assertEqual(various_methods.BespokeMethods.seconds_in(-50), None)

    def test_temperature(self):
        """
        Test - degrees to Fahrenheit
        """
        self.assertEqual(various_methods.BespokeMethods.f2c(212), 100) # Boiling point of water
        self.assertEqual(various_methods.BespokeMethods.f2c(32), 0) # Freezing point of water
        self.assertEqual(various_methods.BespokeMethods.f2c(-40), -40) # Wow, what an interesting case!
        self.assertEqual(various_methods.BespokeMethods.f2c(36), 2)
        self.assertEqual(various_methods.BespokeMethods.f2c(37), 3)
        self.assertEqual(various_methods.BespokeMethods.f2c(38), 3)
        self.assertEqual(various_methods.BespokeMethods.f2c(39), 4)

        self.assertEqual(various_methods.BespokeMethods.c2f(0), 32)
        self.assertEqual(various_methods.BespokeMethods.c2f(100), 212)
        self.assertEqual(various_methods.BespokeMethods.c2f(-40), -40)
        self.assertEqual(various_methods.BespokeMethods.c2f(12), 54)
        self.assertEqual(various_methods.BespokeMethods.c2f(18), 64)
        self.assertEqual(various_methods.BespokeMethods.c2f(-48), -54)


if __name__ == '__main__':
    unittest.main()