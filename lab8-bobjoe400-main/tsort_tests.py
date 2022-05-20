import unittest
from tsort import *

class TestTsort(unittest.TestCase):
        
    def test_01(self):
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = "141\n101\n102\n225\n103\n315\n357"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)        

    def test_02(self):
        input = ['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        expect = "red\ngreen\npurple\nblue\nblack"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_03(self):
        input = ['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']
        expect = "1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_04(self):
        input = ['3', '8', '3', '10', '5', '11', '7', '8', '7', '11', '8', '9', '11', '2', '11', '9', '11', '10']
        expect = "7\n5\n11\n2\n3\n10\n8\n9"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)
    
    def test_notenoughvertices(self):
        input = ['red','3','4','5','6']
        with self.assertRaises(ValueError):
            tsort(input)
    
    def test_cyclicallist(self):
        input = ['3','2','2','1','1','3']
        with self.assertRaises(ValueError):
            tsort(input)
    
    def test_mixed(self):
        input = ['aardvark','blue','clear','blue','blue','down',"this is a test",'aardvark']
        """ 
        ('a','b','c') 1 
        2 2
        'c' 0
        'd' 1
        "this is a test" 0 
        """
        expect = "this is a test\naardvark\nclear\nblue\ndown"
        actual = tsort(input)
        self.assertEqual(actual.strip(),expect)

    def test_spaces(self):
        input = ['\n', 'blah', 'blah', ' ', '\n', '', '', '  ', ' ', '  ']
        expect = '\n\n\nblah\n \n  '
        actual = tsort(input)
        self.assertEqual(actual, expect)

if __name__ == "__main__":
    unittest.main()
