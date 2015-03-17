#! /usr/bin/env python

import pytest
import random
import copy
from mergesort import merge_sort


def test_merge_sort(made_list):
    """Testing that the list is correctly sorted """
    un_sorted = copy.copy(made_list)
    made_list.sort()
    assert merge_sort(un_sorted) == made_list

#####################
# Test Fixtures
#####################


@pytest.fixture(scope='function')
def made_list():
    return random.sample(range(1000), 100)
