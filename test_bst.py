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
    assert a.size() == 5
    a.insert(9)
    #test that a duplicate value does not get added
    assert a.size() == 5


def test_depth(populated_tree):
    assert populated_tree.depth() == 4

def test_depth_empty(empty_tree):
    assert empty_tree.depth() is None

def test_depth_one():
    b = Bst()
    b.insert(100)
    assert b.depth() == 1

def test_balance(populated_tree):
    assert populated_tree.balance() == -2
    b = Bst()
    b.insert(5)
    b.insert(1)
    assert b.balance() == 1


def test_containts(populated_tree):
    assert populated_tree.contains(9)
    assert populated_tree.contains(2) is False


def test_in_order(populated_tree):
    gen = populated_tree.in_order()
    assert next(gen) == 3
    assert next(gen) == 5


def test_pre_order(populated_tree):
    gen = populated_tree.pre_order()
    assert next(gen) == 5
    assert next(gen) == 3
    assert next(gen) == 7
    assert next(gen) == 6

def test_post_order(populated_tree):
    gen = populated_tree.post_order()
    assert next(gen) == 3
    assert next(gen) == 6
    assert next(gen) == 9


def test_breadth_first(populated_tree):
    gen = populated_tree.breadth_first()
    assert next(gen) == 5
    assert next(gen) == 3
    assert next(gen) == 7


def test_deletion(populated_tree):
    """Test deletion of a value"""
    populated_tree.delete(7)
    assert populated_tree.top.right.data == 8
    assert 7 not in populated_tree.set


def test_deletion_bt(big_ass_tree):
    """Test deletion of a value"""
    big_ass_tree.delete(120)
    assert big_ass_tree.top.right.data == 123
    big_ass_tree.delete(25)
    assert big_ass_tree.top.left.right.data == 33


def test_delete_empty(empty_tree):
    """Confirm that a delted node is not tracking in the tree"""
    assert empty_tree.delete(1234) is None


def test_balance_tree(populated_tree):
    """Test that a rebalanced tree has a depth equal to
    the binary power plus one. This ensures balance"""
    a = populated_tree.balance_self()
    assert a.balance() == 0
    assert a.depth() == 3


def test_balance_bigtree(big_ass_tree):
    """duplicate test with a bigger list
    This ensures balance"""
    a = big_ass_tree.balance_self()
    assert a.balance() == 0
    assert a.depth() == 5


def test_balance_tree_zero(empty_tree):
    """Test balance for a empty tree"""
    a = empty_tree.balance_self()
    assert a is None


##################################
# Testing Fixtures
##################################
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


@pytest.fixture(scope='function')
def big_ass_tree():
    tree = Bst()
    tree.insert(100)
    tree.insert(14)
    tree.insert(25)
    tree.insert(77)
    tree.insert(98)
    tree.insert(120)
    tree.insert(33)
    tree.insert(145)
    tree.insert(66)
    tree.insert(111)
    tree.insert(200)
    tree.insert(22)
    tree.insert(188)
    tree.insert(77)
    tree.insert(101)
    tree.insert(84)
    tree.insert(123)
    tree.insert(140)
    tree.insert(20)
    tree.insert(50)
    return tree
