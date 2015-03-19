import pytest
import random
from radixsort import radixsort


def test_empty(empty_list):
    """Test with empty list"""
    assert radixsort(empty_list) == []


def test_sort(sorted_list):
    """Test with sorted list list"""
    assert radixsort(sorted_list) == sorted_list


def test_rand(made_list):
    """Test with random list"""
    assert radixsort(made_list) == sorted(made_list)


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

