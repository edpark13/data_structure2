#! /usr/bin/env python

import pytest
import random
import copy
from mergesort import merge_sort


def test_merge_sort(made_list):
    """Testing that the list is correctly sorted"""
    un_sorted = copy.copy(made_list)
    made_list.sort()
    assert merge_sort(un_sorted) == made_list


def test_empty_sort(empty_list):
    """Testing that an empty list does not error out"""
    assert merge_sort(empty_list) == []


def test_duplicate_values():
    """"Test that sort is stable"""
    l = [1, 2, 2.0, 4, 10, 30, 15, 20]
    assert type(merge_sort(l)[1]) == int
    assert type(merge_sort(l)[2]) == float

#####################
# Test Fixtures
#####################


@pytest.fixture(scope='function')
def made_list():
    return random.sample(range(1000), 100)


@pytest.fixture(scope='function')
def empty_list():
    l = []
    return l
