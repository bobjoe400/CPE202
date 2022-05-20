import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_empties(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.search(10))
        self.assertTrue(bst.find_min() is None)
        self.assertTrue(bst.find_max() is None)
        self.assertTrue(bst.tree_height() is None)
        self.assertEqual(bst.inorder_list(),[])
        self.assertEqual(bst.preorder_list(),[])
        self.assertEqual(bst.level_order_list(), [])

    def test_complex(self):
        bst = BinarySearchTree()
        bst.insert(1, 'hi')
        bst.insert(10,'lol')
        bst.insert(7,'jk')
        bst.insert(-3,'lmao')
        bst.insert(0,'hello')
        bst.insert(2,'jk')
        bst.insert(-3, 'haha')
        self.assertEqual(bst.find_min(), (-3,'haha'))
        bst.insert(10,'heh')
        self.assertEqual(bst.find_max(), (10,'heh'))
        self.assertEqual(bst.level_order_list(), [1,-3,10,0,7,2])
        self.assertEqual(bst.inorder_list(), [-3,0,1,2,7,10])
        self.assertEqual(bst.preorder_list(), [1,-3,0,10,7,2])
        self.assertEqual(bst.tree_height(), 3)
        self.assertTrue(bst.search(2))


if __name__ == '__main__':
    unittest.main()
