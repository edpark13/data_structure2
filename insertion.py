#! /usr/bin/env python

import time


def timed_func(func):
    """Decorator for timing our insertion sort methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "time expired: %s" % elapsed
        return result
    return timed

@timed_func
def insertion_sort(lis):
    """Sorts a given list using an insert method"""
    for x in xrange(len(lis)):
        i = x
        while i > 0 and lis[i-1] > lis[i]:
            lis[i], lis[i-1] = lis[i-1], lis[i]
            i -= 1
    return lis


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


if __name__ == '__main__':
    print "sorted 100"
    insertion_sort(sorted_list(100))
    print "rever sorted 100"
    insertion_sort(reverse_sorted_list(100))
    print "sorted 1000"
    insertion_sort(sorted_list(1000))
    print "rever sorted 1000"
    insertion_sort(reverse_sorted_list(1000))
