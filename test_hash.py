#! /usr/bin/env python

import pytest
from hash_table import Hash_table as Hash


def test_init(empty_table):
    """Test if empty_table contructed properly"""
    assert empty_table.size == 5


def test_hashing(empty_table):
    """Test the hash value of a string"""
    hashed = empty_table.hash('hello')
    assert hashed == 2


def test_set(empty_table):
    """Test if a key and value is properly set in the Hash Table"""
    empty_table.set('hello', 20)
    hashed =  empty_table.hash('hello')
    assert ('hello', 20) in empty_table.table[hashed]

def test_get_key(empty_table):
    """Test if we get the correct value when giving a key"""
    empty_table.set('hello', 20)
    print empty_table.get_key('hello')
    assert 20 == empty_table.get_key('hello')

def test_full_table(full_table):
    """Test a big hash table and test if everything is setting and getting
    correctly"""
    f = open('/usr/share/dict/words').read().splitlines()
    for word in f:
        assert word == full_table.get_key(word)

###################
# Test Setup
###################


@pytest.fixture(scope='function')
def empty_table():
    table = Hash(5)
    return table

@pytest.fixture(scope='session')
def full_table():
    table = Hash(1024)
    f = open('/usr/share/dict/words').read().splitlines()
    for word in f:
        table.set(word, word)
    return table
