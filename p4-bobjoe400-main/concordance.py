import string
import re
from hash_quad import *


class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            file = open(filename)
        except:
            raise FileNotFoundError
        words = file.read().splitlines()
        file.close()
        for word in words:
            word = word.lower()
            self.stop_table.insert(word,words.index(word))

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file = open(filename)
        except:
            raise FileNotFoundError
        self.concordance_table = HashTable(191)
        line = file.readline()
        i = 1
        while line != "":
            line = line.rstrip('\n')
            line = line.replace("'",'')
            puncremove = str.maketrans(string.punctuation,' '*len(string.punctuation))
            line = line.translate(puncremove)
            line = set(line.lower().split())
            for word in line:
                if word.isalpha():
                    if not self.stop_table.in_table(word):
                        #print(word)
                        index = self.concordance_table.get_index(word)
                        if index is not None:
                            self.concordance_table.hash[index][1].append(i)
                        else:
                            self.concordance_table.insert(word,[i])
            line = file.readline()
            i += 1
        file.close()
                
        
    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        keys = sorted(self.concordance_table.get_all_keys())
        values = [self.concordance_table.get_value(key) for key in keys]
        file = open(filename,'w')
        for i in range(0,len(keys)):
            v_str = ' '.join([str(val) for val in values[i]])
            line = ': '.join((keys[i],v_str)) + "\n"
            #print(line)
            file.write(line)
        file.close()