import pytest
import random
from quicksort import quicksort, random_quicksort, median_quicksort

def test_empty(empty_list):
    assert quicksort(empty_list) == empty_list

def test_list(made_list):
    assert quicksort(made_list) == sorted(made_list)

def test_sorted(sorted_list):
    assert quicksort(sorted_list) == sorted_list

def test_random_empty(empty_list):
    assert random_quicksort(empty_list) == empty_list

def test_random_list(made_list):
    assert random_quicksort(made_list) == sorted(made_list)

def test_random_sorted(sorted_list):
    assert random_quicksort(sorted_list) == sorted_list

def test_median_empty(empty_list):
    assert median_quicksort(empty_list) == empty_list

def test_median_list(made_list):
    assert median_quicksort(made_list) == sorted(made_list)

def test_median_sorted(sorted_list):
    assert median_quicksort(sorted_list) == sorted_list


@pytest.fixture(scope='function')
def made_list():
    made_list = random.sample(range(1000), 100)
    print made_list
    return made_list

@pytest.fixture(scope='function')
def sorted_list():
    return range(10)

@pytest.fixture(scope='function')
def empty_list():
    l = []
    return l
