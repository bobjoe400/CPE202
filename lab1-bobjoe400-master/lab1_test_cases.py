# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self):
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_03(self):
        tlist = []
        self.assertEqual(max_list_iter(tlist),None) #check for empty list

    def test_max_list_04(self):
        tlist = [3,2,1]
        self.assertEqual(max_list_iter(tlist),3) #check if the max is in front

    def test_reverse(self):
        intlist = [1, 2, 3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])

    def test_reverse1(self):
        intList = None
        with self.assertRaises(ValueError): #check for exception
            reverse_list(intList)

    def test_reverse_mutate(self):
        intlist = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])

    def test_reverse_mustate1(self):
        intlist = None
        with self.assertRaises(ValueError): #check for exception
            reverse_list_mutate(intlist)

    def test_reverse_mustate2(self):
        intlist = ['a',10,33,'bb',44,"c3",55.2]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [55.2,"c3",44,'bb',33,10,'a']) #check with multiple data types

    def test_reverse_rec(self):
        intlist = [1, 2, 3]
        self.assertEqual(reverse_rec(intlist),[3, 2, 1])
        self.assertEqual(intlist,[1, 2, 3])

    def test_reverse_rec1(self):
        intlist = None
        with self.assertRaises(ValueError): #check for exception
            reverse_rec(intlist)

    def test_reverse_rec(self):
        intlist = ['a',10,33,'bb',44,"c3",55.2]
        self.assertEqual(reverse_rec(intlist), [55.2,"c3",44,'bb',33,10,'a'])
        self.assertEqual(intlist,['a',10,33,'bb',44,"c3",55.2]) #check with multiple data types

if __name__ == "__main__":
        unittest.main()
