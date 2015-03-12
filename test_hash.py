#! /usr/bin/env python

import pytest
from hash_table import Hash_table as Hash


def test_hashing(empty_table):
    assert empty_table.size == 5


def test_hasing(empty_table):
    hashed = empty_table.hash('hello')
    assert hashed == 2


def test_set(empty_table):
    empty_table.set('hello', 20)
    assert True

###################
# Test Setup
###################


@pytest.fixture(scope='function')
def empty_table():
    table = Hash(5)
    return table


