# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        str1 = "Location('SLO', 35.3, -120.7)"
        str2 = "Location(SLO, 35.3, -120.7)"
        res = repr(loc)
        #print(res)
        self.assertTrue(res == str1 or res == str2)

    # Add more tests!
    def test_repr1(self):
        loc = Location("Slo", 35.2+.1, -120.7)
        self.assertTrue(repr(loc) == "Location(Slo, 35.3, -120.7)")
    def test_eq(self):
        loc = Location('SLO',35.3, -120.7)
        self.assertEqual(loc,Location("SLO",34.2+.1+.1+.1+.1+.1+.1+.1+.1+.1+.1+.1,-120.7))
    def test_eq1(self):
        loc = "lmao"
        self.assertFalse(loc==Location('Paris',48.9,2.4))
    def test_init(self):
        loc = Location('J',120,34.2)
        Location.__init__(loc,'H',34,33)
        self.assertEqual(loc,Location('H',34,33))
    def test_init1(self):
        loc = Location("Paris",120.0,34.2)
        self.assertTrue(loc==Location('Paris',120,34.2))
if __name__ == "__main__":
        unittest.main()
