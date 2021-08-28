import unittest
from strspn import *

class TestCases(unittest.TestCase):
   def test_my_strspn_01(self):
      self.assertEqual(my_strspn("calpoly","local"),3)

if __name__ == '__main__':
   unittest.main()
