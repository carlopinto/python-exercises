import unittest

# Remove 'from TimeOfDay' from line below if you want to run this file
# I keep it, so I can run all the tests from VSCode Testing window

import time_of_day

class TestTimeOfDay(unittest.TestCase):

    def test_create_time(self):
        """"""
        time = time_of_day.MyTime(9, 55, 30)

        # check type
        self.assertEqual(type(time), time_of_day.MyTime)

        # string representation of the MyTime object
        self.assertEqual(time.__str__(), "09:55:30")

        self.assertEqual(str(time), "09:55:30")

    def test_create_time_over2460(self):
        """ 
            What if hour is greater than 24 or 
            minute is greater than 60 or 
            second is greater than 60
        """
        time = time_of_day.MyTime(26, 85, 120)

        self.assertEqual(str(time), "03:27:00 (1)")

    def test_create_time_negative_hours(self):
        """"""
        time = time_of_day.MyTime(-9, 55, 30)

        self.assertEqual(str(time), "15:55:30 (-1)")

    def test_create_time_negative_minutes(self):
        """"""
        time = time_of_day.MyTime(9, -55, 30)

        self.assertEqual(str(time), "08:05:30")

    def test_create_time_negative_seconds(self):
        """"""
        time = time_of_day.MyTime(9, 55, -10)

        self.assertEqual(str(time), "09:54:50")

    def test_sum(self):
        """ + operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        sum = time1 + time2
        self.assertEqual(str(sum), "10:45:20")
        sum2 = time1.__add__(time2)
        self.assertEqual(str(sum2), "10:45:20")

    def test_sub(self):
        """ - operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        sub = time1 - time2
        self.assertEqual(str(sub), "08:15:00")
        sub2 = time1.__sub__(time2)
        self.assertEqual(str(sub2), "08:15:00")

    def test_greater_than_equal(self):
        """ >= operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        comp = time1 >= time2
        self.assertEqual(comp, True)
        comp2 = time1.__ge__(time2)
        self.assertEqual(comp2, True)

    def test_greater_than(self):
        """ > operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        comp = time1 > time2
        self.assertEqual(comp, True)
        comp2 = time1.__gt__(time2)
        self.assertEqual(comp2, True)

    def test_less_than_equal(self):
        """ <= operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        comp = time1 <= time2
        self.assertEqual(comp, False)
        comp2 = time1.__le__(time2)
        self.assertEqual(comp2, False)

    def test_less_than(self):
        """ < operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        comp = time1 < time2
        self.assertEqual(comp, False)
        comp2 = time1.__lt__(time2)
        self.assertEqual(comp2, False)

    def test_equal(self):
        """ == operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        comp = time1 == time2
        self.assertEqual(comp, False)
        comp2 = time1.__eq__(time2)
        self.assertEqual(comp2, False)

    def test_not_equal(self):
        """ != operator overloading """
        time1 = time_of_day.MyTime(9, 30, 10)
        time2 = time_of_day.MyTime(1, 15, 10)
        comp = time1 != time2
        self.assertEqual(comp, True)
        comp2 = time1.__ne__(time2)
        self.assertEqual(comp2, True)

    def test_to_seconds(self):
        """"""
        time1 = time_of_day.MyTime(0, 0, 10)
        time2 = time_of_day.MyTime(23, 14, 32)
        seconds1 = time1.to_seconds()
        seconds2 = time2.to_seconds()
        self.assertEqual(seconds1, 10)
        self.assertEqual(seconds2, 83672)

    def test_increment(self):
        """"""
        time = time_of_day.MyTime(9, 30, 10)
        time.increment(150)
        self.assertEqual(str(time), "09:32:40")

    def test_increment_negative(self):
        """"""
        time = time_of_day.MyTime(9, 30, 10)
        time.increment(-150)
        self.assertEqual(str(time), "09:27:40")

    def test_increment_dayafter(self):
        """"""
        time = time_of_day.MyTime(23, 58, 10)
        time.increment(140)
        self.assertEqual(str(time), "00:00:30 (1)")

    def test_increment_daybefore(self):
        """"""
        time = time_of_day.MyTime(00, 00, 10)
        time.increment(-40)
        self.assertEqual(str(time), "23:59:30 (-1)")

    def test_after(self):
        """"""
        time1 = time_of_day.MyTime(0, 0, 10)
        time2 = time_of_day.MyTime(23, 14, 32)

        self.assertEqual(time2.after(time1), True)

    def test_after_different_days(self):
        """"""
        time1 = time_of_day.MyTime(-5, 20, -10)
        time2 = time_of_day.MyTime(29, 14, 32)

        self.assertEqual(time2.after(time1), True)

    def test_between(self):
        """"""
        time1 = time_of_day.MyTime(9, 55, 30)
        time2 = time_of_day.MyTime(15, 20, 40)
        time3 = time_of_day.MyTime(23, 59, 56)

        self.assertEqual(time3.between(time1, time2), False)
        self.assertEqual(time1.between(time2, time3), False)
        # check if you swap time2 and time3
        self.assertEqual(time1.between(time3, time2), False)

        self.assertEqual(time2.between(time1, time3), True)
        # check if you swap time1 and time3
        self.assertEqual(time2.between(time3, time1), True)

    def test_between_different_days(self):
        """"""
        time1 = time_of_day.MyTime(-5, 20, -10)
        time2 = time_of_day.MyTime(29, 14, 32)
        time3 = time_of_day.MyTime(23, 59, 56)

        self.assertEqual(time3.between(time1, time2), True)
        self.assertEqual(time3.between(time2, time1), True)

if __name__ == "__main__":
    unittest.main()