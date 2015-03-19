#! /usr/bin/env python
import math

def radixsort(l):
    digits = int(math.log10(max(l))+1)
    for i in xrange(1, digits+1):
        a = [[] for x in xrange(0, 10)]
        for x in l:
            a[(x%10^i)//(10^(i-1))].append(x)
        l = []
        for i in xrange(10):
            l.extend(a[i])
    return l


if __name__ == '__main__':
    import pdb
    test = [3, 5, 289, 35, 90, 113]
    # pdb.set_trace()
    print radixsort(test)
    print sorted(test)
