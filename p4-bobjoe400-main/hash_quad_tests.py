import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertFalse(ht.in_table("dog"))

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)
        ht.insert("cat",6)
        self.assertEqual(ht.get_value("cat"), 6)
        self.assertTrue(ht.get_value("dog") is None)

    def test_01g(self):
        ht = HashTable(7)
        for i in range(0,10):
            ht.insert("cat", i)
        self.assertEqual(ht.get_index("cat"), 3)
        self.assertTrue(ht.get_index("dog") is None)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0) 
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0) # Causes rehash        
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)
        
    def test_03(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("abciejnf"), ht.horner_hash("abciejnfiwlakdiewnrjnf"))
        self.assertEqual(ht.horner_hash(""),0)
        self.assertEqual(ht.next_prime(7), 11)
        test = [chr(i) for i in range(97,97+26)]
        test2 = []
        for i in range(0,len(test)):
            word = ""
            for j in range(0,len(test)):
                word+=test[i-j]
            test2.append(word)
        for i in test2:
            ht.insert(i)
        self.assertEqual(set(ht.get_all_keys()), set(test2))
        self.assertEqual(ht.get_num_items(), 26)
        self.assertEqual(ht.get_table_size(), 79)
        self.assertAlmostEqual(ht.get_load_factor(), 26/79)

if __name__ == '__main__':
   unittest.main()