#Michelle Tan
#10/23/2020
#Lab 5

import unittest
import map
import point

class TestCases(unittest.TestCase):
   #Tests all map functions with at two test cases each
   def test_square_all_1(self):
      self.assertEqual(map.square_all([1,3,5,7]),[1,9,25,49])

   def test_square_all_2(self):
      self.assertEqual(map.square_all([2,4,6,8]),[4,16,36,64])

   def test_add_n_all_1(self):
      self.assertEqual(map.add_n_all([35,6,2,56],4),[39,10,6,60])

   def test_add_n_all_2(self):
      self.assertEqual(map.add_n_all([7,52,31,8],8),[15,60,39,16])

   def test_distance_all_1(self):
      self.assertEqual(map.distance_all([[3,2],[3,4],[5,5]]),[3.61, 5.0, 7.07])

   def test_distance_all_2(self):
      self.assertEqual(map.distance_all([[7,4],[26,4],[7,43]]),[8.06, 26.31, 43.57])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
