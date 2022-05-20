import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
    def test_simple2(self):
        nums = [23,10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 2)
        self.assertEqual(nums, [10,23])

if __name__ == '__main__': 
    unittest.main()
