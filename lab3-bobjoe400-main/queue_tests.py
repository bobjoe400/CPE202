import unittest
#from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(None)
        q.enqueue(2)
        q.enqueue(False)
        q.enqueue('Hello')
        q.enqueue('2')
        self.assertEqual(q.size(), 5)
        self.assertTrue(q.is_full())
        self.assertTrue(q.dequeue() is None)
        self.assertEqual(q.dequeue(),2)
        self.assertEqual(q.dequeue(),False)
        self.assertEqual(q.dequeue(),'Hello')
        self.assertEqual(q.dequeue(),'2')
        self.assertTrue(q.is_empty())
        q.enqueue('bar')
        q.enqueue('foo')
        self.assertEqual(q.dequeue(),'bar')
        self.assertEqual(q.size(),1)
    def test_queue2(self):
        q = Queue(0)
        self.assertTrue(q.is_empty())
        self.assertTrue(q.is_full())
        with self.assertRaises(IndexError) as context:
            q.enqueue('foo')
        with self.assertRaises(IndexError) as context:
            q.dequeue()

if __name__ == '__main__': 
    unittest.main()
