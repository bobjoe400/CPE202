# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("12.0 3.2 / 1 +"), 4.75)
        self.assertAlmostEqual(postfix_eval("2 0.5 **"), 1.41421356)
        self.assertAlmostEqual(postfix_eval("3 4 2 * 1 5 - 2 3 ** ** / +"),3)
        self.assertAlmostEqual(postfix_eval("3 2 <<"),12)

    def test_postfix_eval_02(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("blah")
        self.assertEqual(str(e.exception), "Invalid token")

    def test_postfix_eval_03(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("4 +")
        self.assertEqual(str(e.exception), "Insufficient operands")

    def test_postfix_eval_04(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("1 2 3 +")
        self.assertEqual(str(e.exception), "Too many operands")

    def test_postfix_eval_05(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("3 3 / 1 >>")
        self.assertEqual(str(e.exception), "Illegal bit shift operand")

    def test_postfix_eval_06(self):
        with self.assertRaises(PostfixFormatException) as e:
            postfix_eval("      \n\n\n     ")
        self.assertEqual(str(e.exception), "Empty input")

    def test_postfix_eval_07(self):
        with self.assertRaises(ValueError) as e:
            postfix_eval("1 1 + 2 - 0 /")
        self.assertEqual(str(e.exception), "Cannot divide by zero")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("( )"),'')
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"),'3 4 2 * 1 5 - 2 3 ** ** / +')
        self.assertEqual(infix_to_postfix("6 + 3 - 7 * 3 + 2"),'6 3 + 7 3 * - 2 +')

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
