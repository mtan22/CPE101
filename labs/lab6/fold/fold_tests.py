#Michelle Tan
#10/27/2020
#Lab 6

import unittest
from fold import *

class TestCases(unittest.TestCase):
   #Test fold functions with at least two test cases
   def test_sum_1(self):
      self.assertEqual(sum([1,2,4,5,2]),14)

   def test_sum_2(self):
      self.assertEqual(sum([3,5,2,1]),11)

   def test_sum_3(self):
      self.assertEqual(sum([4,6,2]),12)

   def test_index_of_smallest_1(self):
      self.assertEqual(index_of_smallest([1,6,4,-7]),3)

   def test_index_of_smallest_2(self):
      self.assertEqual(index_of_smallest([-3,6,-3,2]),0)

   def test_index_of_smallest_3(self):
      self.assertEqual(index_of_smallest([]),-1)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
