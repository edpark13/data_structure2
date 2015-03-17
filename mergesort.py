#! /usr/bin/env python
import time
from list import makelist


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
    if len(l) <= 1:
        return l
    else:
        left = l[:len(l)/2]
        right = l[len(l)/2:]

        left = merge_sort(left)
        right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
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


@timed_func
def merge_sort_timer(l):
    return merge_sort(l)

if __name__ == "__main__":
    l = sorted_list(100)
    # print 'before sort' + str(l)
    l = merge_sort_timer(l)
    # print 'after sort' + str(l)
    l = merge_sort_timer(reverse_sorted_list(100))
    m = makelist(100)
    m = merge_sort_timer(m)






