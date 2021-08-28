#Project 1
#
#Name: Michelle Tan
#Instructor: Turner
#Section:  01

import unittest
import funcs

class TestCases(unittest.TestCase):
   #At least two test cases to test each function from funcs.py
   def test_poundsToKG_1(self):
      self.assertAlmostEqual(funcs.poundsToKG(0), 0.0)

   def test_poundsToKG_2(self):
      self.assertAlmostEqual(funcs.poundsToKG(120), 54.43104)
      
   def test_getMassObject_1(self):
      self.assertEqual(funcs.getMassObject('t'), 0.1)

   def test_getMassObject_2(self):
      self.assertEqual(funcs.getMassObject('p'), 1.0)

   def test_getMassObject_3(self):
      self.assertEqual(funcs.getMassObject('r'), 3.0)

   def test_getMassObject_4(self):
      self.assertEqual(funcs.getMassObject('g'), 5.3)

   def test_getMassObject_5(self):
      self.assertEqual(funcs.getMassObject('l'), 9.07)

   def test_getMassObject_6(self):
      self.assertEqual(funcs.getMassObject('z'), 0.0)
      
   def test_getVelocityObject_1(self):
      self.assertAlmostEqual(funcs.getVelocityObject(0), 0.0)
   
   def test_getVelocityObject_2(self):
      self.assertAlmostEqual(funcs.getVelocityObject(30), 12.12435565298214)

   def test_getVelocityObject_3(self):
      self.assertAlmostEqual(funcs.getVelocityObject(50), 15.652475842498529)
           
   def test_getVelocitySkater_1(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(100, 0, 100), 0.0) 

   def test_getVelocitySkater_2(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(68 , 5, 12), 0.882)    

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

