#Michelle Tan
#Instructor: Turner
#Section: 01#
#Lab 3

import unittest
from logic import *

class TestCases(unittest.TestCase):
     #Testing the is_even function using an even, odd, negative even, negative odd number
     def test_is_even_1(self):
         self.assertTrue(is_even(2))

     def test_is_even_2(self):
         self.assertTrue(is_even(-8))

     def test_is_even_3(self):
         self.assertFalse(is_even(73))

     def test_is_even_4(self):
         self.assertFalse(is_even(-35))

     #Testing the in_an_interval function using all endpoints, numbers in between the interval, and numbers outside the interval
     def test_in_an_interval_1(self):
         self.assertTrue(in_an_interval(2))

     def test_in_an_interval_2(self):
         self.assertTrue(in_an_interval(6))

     def test_in_an_interval_3(self):
         self.assertFalse(in_an_interval(9))

     def test_in_an_interval_4(self):
         self.assertFalse(in_an_interval(47))

     def test_in_an_interval_5(self):
         self.assertTrue(in_an_interval(64))

     def test_in_an_interval_6(self):
         self.assertFalse(in_an_interval(92))

     def test_in_an_interval_7(self):
         self.assertFalse(in_an_interval(12))

     def test_in_an_interval_8(self):
         self.assertTrue(in_an_interval(18))

     def test_in_an_interval_9(self):
         self.assertTrue(in_an_interval(19))

     def test_in_an_interval_10(self):
         self.assertTrue(in_an_interval(101))

     def test_in_an_interval_11(self):
         self.assertTrue(in_an_interval(102))

     def test_in_an_interval_12(self):
         self.assertTrue(in_an_interval(103))

     def test_in_an_interval_13(self):
         self.assertFalse(in_an_interval(104))

     def test_in_an_interval_14(self):
         self.assertFalse(in_an_interval(0))

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
