import unittest
import filecmp
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_lt_and_eq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(ascii, freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode(101, 0)), 0)
        self.assertEqual(lst.index(HuffmanNode(100, 16)), 6)
        self.assertEqual(lst.index(HuffmanNode(97, 2)), 2)
        self.assertFalse(HuffmanNode(97, 2) is None)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')
            
    def test_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()        
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_multilinefile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_emptyfile(self):
        huffman_encode("empty_file.txt", "empty_file_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_file_out.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb empty_file_out_compressed.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)

    def test_05_onecharfile(self):
        huffman_encode("one_char.txt", "one_char_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb one_char_out.txt one_char_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb one_char_out_compressed.txt one_char_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)
     
    def test_06_textfile_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07_textfile_decode(self):
        huffman_decode("file2_compressed_soln.txt", "file2_decoded.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2.txt file2_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_08_multilinefile_decode(self):
        huffman_decode("multiline_compressed_soln.txt", "multiline_decoded.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline.txt multiline_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_09_emptyfile_decode(self):
        huffman_decode("empty_file.txt", "empty_file_decoded.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_file.txt empty_file_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_10_onecharfile_decode(self):
        huffman_decode("one_char_compressed_soln.txt", "one_char_decoded.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb one_char.txt one_char_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_11_filenotfound(self):
        with self.assertRaises(FileNotFoundError):
            freqlist = cnt_freq("nofile.txt")
        with self.assertRaises(FileNotFoundError):
            huffman_encode("nofile.txt",'nofile_out.txt')
        with self.assertRaises(FileNotFoundError):
            huffman_decode("nofile.txt",'nofile_out.txt')
            
    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)   

if __name__ == '__main__':
   unittest.main()
