#! /usr/bin/env python

import pytest
from bst import Bst


def test_constructor():
    instance = Bst()
    assert type(instance) is Bst


def test_insert(empty_tree):
    a = empty_tree
    a.insert(5)
    a.insert(7)
    assert 7 is a.top.right.data
    a.insert(8)
    a.insert(6)
    a.insert(9)
    assert a.top.data == 5
    a.insert(9)
    #test that a duplicate value does not get added
    assert a.size() == 5


def test_depth(populated_tree):
    assert populated_tree.depth == 4


def test_balance(populated_tree):
    assert populated_tree.balance() == 2


def test_containts(populated_tree):
    assert populated_tree.contains(9)
    assert populated_tree.contains(2) is False


@pytest.fixture(scope='function')
def populated_tree():
    tree = Bst()
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)
    tree.insert(9)
    tree.insert(3)
    return tree


@pytest.fixture(scope='function')
def empty_tree():
    tree = Bst()
    return tree



