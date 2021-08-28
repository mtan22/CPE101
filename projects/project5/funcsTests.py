#Project 5 - File Matching
#Name: Michelle Tan
#Date: November 27, 2020
#Section: 01
#Instructor: Prof. Turner

import unittest
from fileMatchingFuncs import *

class TestCases(unittest.TestCase):
   #Methods below run at least two test cases for functions applicable
   def test_entry_init(self):
      entry = Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO')
      self.assertEqual(entry.account_num, '345')
      self.assertEqual(entry.name, 'Bob Jones')
      self.assertAlmostEqual(entry.balance, 87.12)
      self.assertEqual(entry.phone, '8055551234')
      self.assertEqual(entry.city, 'SLO')   

   def test_read_file_0(self):
      entries = [['100', 'Alan', 'Jones', '348.17', '8053564820', 'SLO'],['700', 'Suzy', 'Green', '-14.22', '8052586912', 'SLO']]
      self.assertEqual(read_file('test0.dat'), entries)

   def test_read_file_1(self):
      entries = [['100', 'Alan', 'Jones', '348.17', '8053564820', 'SLO'],['700', 'Suzy', 'Green', '-14.22', '8052586912', 'SLO'],['300', 'Mary', 'Smith','27.19', '8057901237', 'Santa_Maria'],['800', 'Mike', 'Rosen', '-104.58', '8051200891','Pismo_Beach']]
      self.assertEqual(read_file('test1.dat'), entries)

   def test_sort_file_0(self):
      self.assertEqual(sort_file(read_file('test0.dat')), [['100', 'Alan', 'Jones', '348.17', '8053564820', 'SLO'], ['700', 'Suzy', 'Green', '-14.22', '8052586912', 'SLO']]) 

   def test_sort_file_1(self):
      self.assertEqual(sort_file(read_file('test1.dat')), [['100','Alan','Jones','348.17','8053564820','SLO'],['300','Mary','Smith','27.19','8057901237','Santa_Maria'],['700','Suzy','Green','-14.22','8052586912','SLO'],['800','Mike','Rosen','-104.58','8051200891','Pismo_Beach']])

   def test_sort_file_2(self):
      self.assertEqual(sort_file(read_file('oldMaster.dat')), [['100', 'Alan', 'Jones', '348.17', '8053564820', 'SLO'],['120', 'Ford', 'Strong', '90.00', '8051155329', 'SLO'],['200', 'Adam', 'Wise', '100.00', '8059867128', 'SLO'],['300', 'Mary', 'Smith', '27.19', '8057901237', 'Santa_Maria'],['340', 'Lena', 'Sharp', '70.00', '8058561859', 'SLO'],['500', 'Sam', 'Sharp', '0.00', '8052348970', 'SLO'],['600', 'Nicol', 'Green', '-20.00', '8058875571', 'SLO'],['700', 'Suzy', 'Green', '-14.22', '8052586912', 'SLO'],['800', 'Mike', 'Rosen', '-104.58', '8051200891', 'Pismo_Beach']])
     
   def test_sort_acc_nums_0(self):
      self.assertEqual(sort_acc_nums(read_file('test0.dat')), [100, 700])
   
   def test_sort_acc_nums_1(self):
      self.assertEqual(sort_acc_nums(read_file('test1.dat')), [100, 300, 700, 800])

   def test_sort_acc_nums_2(self):
      self.assertEqual(sort_acc_nums(read_file('oldMaster.dat')), [100, 120, 200, 300, 340, 500, 600, 700, 800])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

