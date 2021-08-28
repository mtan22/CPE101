#Michelle Tan
#10/27/2020
#Lab 6

import unittest
from string_101 import *

class TestString(unittest.TestCase):
   #Test string_101 functions using at least two test cases
   def test_str_rot_13_1(self):
      self.assertEqual(str_rot_13('abegea'),'nortrn')

   def test_str_rot_13_2(self):
      self.assertEqual(str_rot_13('EGAsg0'),'RTNft0')

   def test_str_rot_13_3(self):
      self.assertEqual(str_rot_13('GeageE48'),'TrntrR48')

   def test_str_translate_101_1(self):
      self.assertEqual(str_translate_101('abcdcba','a','x'),'xbcdcbx')

   def test_str_translate_101_2(self):
      self.assertEqual(str_translate_101('geagev','g','P'),'PeaPev')

   def test_str_translate_101_3(self):
      self.assertEqual(str_translate_101('K83bsgsue','s','M'),'K83bMgMue')

if __name__ == '__main__':
   unittest.main()
