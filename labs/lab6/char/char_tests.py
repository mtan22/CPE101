#Michelle Tan
#10/27/2020
#Lab 6

import unittest
from char import *

class TestChar(unittest.TestCase):
   #Test char functions with at least two test cases
   def test_is_lower_101_1(self):
      self.assertEqual(is_lower_101('a'),True)

   def test_is_lower_101_2(self):
      self.assertEqual(is_lower_101('B'),False)

   def test_is_lower_101_3(self):
      self.assertEqual(is_lower_101('c'),True)

   def test_char_rot_13_1(self):
      self.assertEqual(char_rot_13('a'),'n')

   def test_char_rot_13_2(self):
      self.assertEqual(char_rot_13('N'),'A')

   def test_char_rot_13_3(self):
      self.assertEqual(char_rot_13('B'),'O')

if __name__ == '__main__':
   unittest.main()
