import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_create1(self):
        self.assertTrue(createlist(1)==[])
    def test_create2(self):
        self.assertTrue(createlist(42)==[42])
    def test_create3(self):
        self.assertTrue(createlist(104)==[104,52,42])

if __name__ == "__main__":
    unittest.main()
