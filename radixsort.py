#! /usr/bin/env python
import math
import random

def radixsort(l):
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
    randoml = random.sample(range(100), 10)
    print radixsort(randoml)
    print sorted(randoml)
