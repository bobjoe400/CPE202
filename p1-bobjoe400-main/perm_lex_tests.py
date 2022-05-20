import unittest
import perm_lex

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
    def test_perm_gen_lex1(self):
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
    def test_perm_gen_lex2(self):
        self.assertEqual(perm_lex.perm_gen_lex('abcd'),['abcd','abdc','acbd','acdb','adbc','adcb','bacd','badc','bcad','bcda','bdac','bdca','cabd','cadb','cbad','cbda','cdab','cdba','dabc','dacb','dbac','dbca','dcab','dcba'])
if __name__ == "__main__":
        unittest.main()
