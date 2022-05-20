import unittest

# Use the imports below to test either your array-based stack
# or your link-based version

#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    def test_empty_stack(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(),0)
    def test_full(self):
        stack = Stack(4)
        self.assertFalse(stack.is_full())
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        stack.push('foo')
        stack.push(False)
        stack.push(None)
        self.assertEqual(stack.pop(),None)
        self.assertEqual(stack.peek(), False)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(),False)
        stack.push('hello')
        stack.push('hi')
        self.assertEqual(stack.peek(), 'hi')
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError) as context:
            stack.push('bar')
        self.assertEqual(stack.size(),4)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        with self.assertRaises(IndexError) as context:
            stack.pop()
        with self.assertRaises(IndexError) as context:
            stack.peek()
if __name__ == '__main__':
    unittest.main()
