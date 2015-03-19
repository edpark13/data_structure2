#! /usr/bin/env python
import math
import random
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
def radixsort(l):
    """Implemented Radix Sort using math notation"""
    try:
        digits = int(math.log10(max(l))+1)
        for i in xrange(1,digits+1):
            ll = [[] for p in xrange(0,10)]
            # import pdb; pdb.set_trace()
            for x in l:
                ll[x%10**i//(10**(i-1))].append(x)
            l = []
            for j in xrange(10):
                l.extend(ll[j])
        return l
    except ValueError:
        return []


if __name__ == '__main__':
    randoml = random.sample(range(1000), 100)
    print radixsort(randoml)
    print "Radix with sorted list"
    sorted_list = sorted(randoml)
    print radixsort(sorted_list)


