#! /usr/bin/env python


class Hash_table(object):
    """Implement a Hash and store a key and a value"""

    def __init__(self, size):
        self.size = size
        self.table = [[] for x in xrange(size)]

    def get_key(self, key):
        """Given a key get the value associated with that key"""
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        for tup in bucket:
            if tup[0] == key:
                return tup[1]

    def set(self, key, value):
        """Add a key and value pair into the Hash Table"""
        if type(key) == str:
            hashed_key = self.hash(key)
            self.table[hashed_key].append((key, value))
        else:
            raise TypeError('Keys must be strings')

    def hash(self, key):
        """Given a key the hashed number of that key"""
        hash_value = 0
        for i in key:
            hash_value += ord(i)
        modulated_hash = hash_value % self.size
        return modulated_hash


