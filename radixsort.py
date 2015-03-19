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


def radixsort_string(l, index=0):
    if len(l) > 2:
        r = []
        ll = [[] for i in xrange(26)]
        for word in l:
            if index < len(word):
                lower_word = word.lower()
                ll[ord(lower_word[index]) - 97].append(word)
            else:
                r.append(word)
        for i in xrange(26):
            r.extend(radixsort_string(ll[i], index+1))
        return r
    return l

if __name__ == '__main__':
    # randoml = random.sample(range(1000), 100)
    # print radixsort(randoml)
    # print "Radix with sorted list"
    # sorted_list = sorted(randoml)
    # print radixsort(sorted_list)
    l = ['asdf', 'u', 'a', 'bqwg', 'iuhjnewfsadfb']
    print radixsort_string(l)
