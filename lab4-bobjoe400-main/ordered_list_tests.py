import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):
    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_complex(self):
        list = OrderedList()
        list.add(0)
        list.add(-3)
        list.add(5)
        list.add(4)
        list.add(7)
        list.add(3.5)
        self.assertFalse(list.add(7))
        self.assertEqual(list.python_list(),[-3,0,3.5,4,5,7])
        self.assertEqual(list.size(),6)
        with self.assertRaises(IndexError):
            list.pop(6)
        self.assertEqual(list.pop(3),4) #[-3,0,3.5,5,7]
        self.assertEqual(list.pop(0),-3) #[0,3.5,5,7]
        self.assertEqual(list.pop(0),0) #[3.5,5,7]
        with self.assertRaises(IndexError):
            list.pop(3)
        list.add(40000)
        self.assertTrue((list.index(8) is None))
        self.assertFalse(list.search(8))
        self.assertFalse(list.remove(3.6))
        self.assertTrue(list.remove(40000))
        self.assertEqual(list.index(3.5),0)
        self.assertTrue(list.search(7))
        self.assertEqual(list.size(),3)
        self.assertEqual(list.python_list(),[3.5,5,7])
        self.assertEqual(list.python_list_reversed(),[7,5,3.5])
        while not list.is_empty():
            list.pop(0)
        with self.assertRaises(IndexError):
            list.pop(0)
        self.assertEqual(list.python_list(),[])
        self.assertEqual(list.python_list_reversed(),[])

if __name__ == '__main__':
    unittest.main()
