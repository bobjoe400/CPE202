# -*- coding: utf-8 -*-
from math import sqrt

class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will 
            be used, if 11 is passed, 11 will be used.)'''
        self.hash = self.next_prime(table_size, True)*[None]
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        index = test = self.horner_hash(key)%self.get_table_size()
        i = 1
        while self.hash[test]:
            if self.hash[test][0] == key:
                self.num_items -= 1
                break
            test = (index + i*i)%self.get_table_size()
            i += 1
        index = test
        self.num_items += 1
        self.hash[index] = [key, value]

        if self.get_load_factor() > 0.5:
            tempHash = HashTable(2*self.get_table_size())
            for data in self.hash:
                if data:
                    tempHash.insert(data[0],data[1])
            self.hash = tempHash.hash                

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.'''
        P = 31
        n = min(len(key),8)
        hashvalue = 0
        for i in range(0,n):
            hashvalue = P*hashvalue + ord(key[i])
        return hashvalue

    def next_prime(self, n, init = False):
        ''' Find the next prime number that is > n.'''
        def is_prime(n):
            if n in (2, 3, 5, 7, 11):  # special case small primes
                return True
            if n % 2 == 0 or n == 1:  # special case even numbers and 1
                return False
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        found = False
        while not found:
            if init:
                if is_prime(n):
                    found = True
                else:
                    n += 1
            else:
                n += 1
                if is_prime(n):
                    found = True
        return n

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        if self.get_index(key) is None:
            return False
        return True

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        h_hash = test= self.horner_hash(key)%self.get_table_size()
        i = 1
        while self.hash[test]:
            if self.hash[test][0] == key:
                return test
            test = (h_hash +i*i)%self.get_table_size()
            i+=1
        return None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        retlist = []
        for i in list(filter(None,self.hash)):
            retlist.append(i[0])
        return retlist

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.get_index(key)
        if index is not None:
            return self.hash[index][1]
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return len(self.hash)

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.get_num_items()/self.get_table_size()