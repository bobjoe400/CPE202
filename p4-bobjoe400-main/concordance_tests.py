# -*- coding: utf-8 -*-
import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):


    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)
        
    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_fileNotFoundstoptable(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("notafile.txt")
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table("notafile.txt")
    
    def test_empty(self):
        conc = Concordance()
        conc.load_stop_table("empty_file.txt")
        conc.load_concordance_table("empty_file.txt")
        conc.write_concordance("empty_file_con.txt")
        err = subprocess.call("diff -wb empty_file_con.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)

    def test_one_word(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("one_word_many.txt")
        test = Concordance()
        test.load_stop_table("stop_words.txt")
        test.load_concordance_table("one_word_few.txt")
        self.assertEqual(conc.concordance_table.get_index("abracadabra"),test.concordance_table.get_index("abracadabra"))
        conc.write_concordance("one_word_con.txt")
        err = subprocess.call("diff -wb one_word_con.txt one_word_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_stop_words(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("stop_text.txt")
        conc.write_concordance("stop_text_con.txt")
        err = subprocess.call("diff -wb stop_text_con.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)
    
    def test_punctuation(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("punc.txt")
        conc.write_concordance("punc_con.txt")
        err = subprocess.call('diff -wb punc_sol.txt punc_con.txt',shell= True)
        self.assertEqual(err,0)

    """ def test_big(self):
        import time
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        start_time = time.time()
        conc.load_concordance_table("War_And_Peace.txt")
        print(time.time()-start_time)
        start_time = time.time()
        conc.write_concordance("War_And_Peace_con.txt")
        print(time.time()-start_time)
        err = subprocess.call("diff -wb War_And_Peace_sol.txt War_And_Peace_con.txt", shell = True)
        self.assertEqual(err, 0) """

if __name__ == '__main__':
    unittest.main()
