import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)

   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62,10),1.62)

   def test_update_alt1(self):
      self.assertAlmostEqual(updateAltitude(135.33,33.53,1.53),169.62)

   def test_update_alt2(self):
      self.assertAlmostEqual(updateAltitude(120.64,24.35,1.75),145.87)

   def test_update_vel1(self):
      self.assertAlmostEqual(updateVelocity(35.646,1.77),37.42)
   
   def test_update_vel2(self):
      self.assertAlmostEqual(updateVelocity(46.347,1.63),47.98)

   def test_update_fuel1(self):
      self.assertAlmostEqual(updateFuel(50,8),42)

   def test_update_fuel2(self):
      self.assertAlmostEqual(updateFuel(64,9),55)

#Testing functions that calculate
if __name__ == '__main__':
   unittest.main()

