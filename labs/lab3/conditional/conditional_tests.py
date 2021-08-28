#Michelle Tan
#Instructor: Turner
#Section: 01
#Lab 3

import unittest
from conditional import *

class TestCases(unittest.TestCase):
    #Tests max_101 function with various values including the same x and y value and other various values
    def test_max_101_1(self):
        self.assertEqual(max_101(0,0),0)

    def test_max_101_2(self):
        self.assertEqual(max_101(0,4),4)

    def test_max_101_3(self):
        self.assertEqual(max_101(3,-64),3)

    #Tests max_of_three function with various values including the same x, y, and z value with other various values
    def test_max_of_three_1(self):
        self.assertEqual(max_of_three(0,0,0),0)

    def test_max_of_three_2(self):
        self.assertEqual(max_of_three(2,6,4),6)

    def test_max_of_three_3(self):
        self.assertEqual(max_of_three(34,2,-3),34)

    def test_max_of_three_4(self):
        self.assertEqual(max_of_three(-42,-89,-2),-2)

    #Tests rental_late_fee function with values from each interval
    def test_rental_late_fee_1(self):
        self.assertEqual(rental_late_fee(8),5)

    def test_rental_late_fee_2(self):
        self.assertEqual(rental_late_fee(15),7)

    def test_rental_late_fee_3(self):
        self.assertEqual(rental_late_fee(0),0)

    def test_rental_late_fee_4(self):
        self.assertEqual(rental_late_fee(35),100)

    def test_rental_late_fee_5(self):
        self.assertEqual(rental_late_fee(16), 19)

    def test_rental_late_fee_6(self):
        self.assertEqual(rental_late_fee(24), 19)

if __name__ == '__main__':
    unittest.main()
