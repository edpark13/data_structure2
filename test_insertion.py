import pytest
from insertion import insertion_sort

@pytest.fixture(scope='function')
def made_list():
    l = [4, 7, 3, 8, 1, 9]
    return l

@pytest.fixture(scope='function')
def dupe_list():
    l = [4, 7, 3, 8, 1, 9, 1, 3]
    return l

@pytest.fixture(scope='function')
def ordered_list():
    l = [0, 1, 2, 3, 4]
    return l

def test_insertion_sort_ml(made_list):
    l = made_list
    insertion_sort(l)
    assert l == [1, 3, 4, 7, 8, 9]

def test_insertion_sort_ol(ordered_list):
    l = ordered_list
    insertion_sort(l)
    assert l == [0, 1, 2, 3, 4]

def test_empty():
    l = []
    insertion_sort(l)
    assert l == []

def test_dupe(dupe_list):
    l = dupe_list
    insertion_sort(l)
    assert l ==[1, 1, 3, 3, 4, 7, 8, 9]
