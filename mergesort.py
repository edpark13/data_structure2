#! /usr/bin/env python
import time
from bst import Bst
from list import makeworstlist



def timed_func(func):
    """Decorator for timing our insertion sort methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "time expired: %s" % elapsed
        return result
    return timed


def merge_sort(l):
    """Sorts a list using a simple merge sort implemetnation"""
    if len(l) <= 1:
        return l
    else:
        left = l[:len(l)/2]
        right = l[len(l)/2:]

        left = merge_sort(left)
        right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """Combines two lists lowest to greates
    is a stable merge method"""
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def sorted_list(Number_of_items=100):
    """Creats a list of numbers around the given input"""
    lis = []
    for i in range(Number_of_items):
        lis.append(i)
    return lis


def reverse_sorted_list(Number_of_items=100):
    """Creats a worst case list around the given input"""
    lis = sorted_list(Number_of_items)[::-1]
    return lis


def build_tree(number):
    """Tried using a balanced search tree
    data was not determinate for numbers smaller than
    10,000 to time consuming over 10,000"""
    tree = Bst()
    for i in xrange(number):
        tree.insert(i)
    sorted_tree = tree.balance_self()
    a = []
    for i in sorted_tree.breadth_first():
        a.append(i)
    return a


@timed_func
def merge_sort_timer(l):
    return merge_sort(l)

if __name__ == "__main__":
    l = sorted_list(1000)
    print 'sorted list'
    l = merge_sort_timer(l)
    print 'reverse sorted list'
    l = merge_sort_timer(reverse_sorted_list(1000))
    m = makeworstlist(1000)
    print 'worst case Edward even/odd short'
    m = merge_sort_timer(m)

    # For multiple testes values 100-30,000 the differences is only marginal.
    # For values over 30,000 the calcualtion is too time consuming.
    # Relationship seems to be O(nlogn)





