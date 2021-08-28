#Michelle Tan
#10/23/2020
#Lab 5

import unittest
import filter
import point

class TestCases(unittest.TestCase):
   #Tests all filter functions with two test cases each
   def test_are_positive_1(self):
      self.assertEqual(filter.are_positive([-3,4,6,3,-3]),[4,6,3])

   def test_are_positive_2(self):
      self.assertEqual(filter.are_positive([3,-5,4,-3]),[3,4])

   def test_are_greater_than_1(self):
      self.assertEqual(filter.are_greater_than([5,9,72,2],7),[9,72])

   def test_are_greater_than_2(self):
      self.assertEqual(filter.are_greater_than([42,4,135,3253,342,46],244),[3253,342])

   def test_are_in_first_quadrant_1(self):
      self.assertEqual(filter.are_in_first_quadrant([[-3,5],[6,74],[4,-4],[-42,-56]]),[[6,74]])

   def test_are_in_first_quadrant_2(self):
      self.assertEqual(filter.are_in_first_quadrant([[342,35],[5,-3],[66,4]]),[[342,35],[66,4]])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
