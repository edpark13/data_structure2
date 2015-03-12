#! /usr/bin/env python


class Hash_table(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for x in xrange(size)]

    def get_key(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        [answer for answer, v in enumerate(bucket) if v[0] == key]
        return answer

    def set(self, key, value):
        if type(key) == str:
            hashed_key = self.hash(key)
            self.table[hashed_key].append((key, value))
        else:
            raise TypeError('Keys must be strings')

    def hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
        modulated_hash = hash_value % self.size
        return modulated_hash


