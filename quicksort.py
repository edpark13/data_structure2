#! /usr/bin/env python
import time
import random

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
def quicksort_wrapper(l):
    return quicksort(l)

def quicksort(l):
    if len(l) > 1:
        pivot = l[0]
        left = []
        right = []
        for i in xrange(1,len(l)):
            if l[i] <= pivot:
                left.append(l[i])
            else:
                right.append(l[i])
        sortedleft = quicksort(left)
        sortedright = quicksort(right)

        sortedleft.append(pivot)
        sortedleft.extend(sortedright)

        return sortedleft
    else:
        return l


@timed_func
def random_quicksort_wrapper(l):
    return random_quicksort(l)

def random_quicksort(l):
    if len(l) > 1:
        # l = l[:]
        rand = random.randint(0, len(l) - 1)
        # pivot = l.pop(rand)
        pivot = l[rand]
        left = []
        right = []
        for i in xrange(rand):
            if l[i] <= pivot:
                left.append(l[i])
            else:
                right.append(l[i])
        for i in xrange(rand + 1, len(l)):
            if l[i] <= pivot:
                left.append(l[i])
            else:
                right.append(l[i])
        sortedleft = random_quicksort(left)
        sortedright = random_quicksort(right)

        sortedleft.append(pivot)
        sortedleft.extend(sortedright)

        return sortedleft
    else:
        return l


@timed_func
def median_quicksort_wrapper(l):
    return median_quicksort(l)


def median_quicksort(l):
    if len(l) > 1:
        l = l[:]
        pivotlist = []
        pivotlist.append(l[0])
        pivotlist.append(l[len(l) - 1])
        pivotlist.append(l[len(l) / 2])
        pivot = select_pivot(pivotlist)
        l.remove(pivot)
        left = []
        right = []
        for i in xrange(0, len(l)):
            if l[i] <= pivot:
                left.append(l[i])
            else:
                right.append(l[i])
        sortedleft = median_quicksort(left)
        sortedright = median_quicksort(right)

        sortedleft.append(pivot)
        sortedleft.extend(sortedright)

        return sortedleft
    else:
        return l  

def select_pivot(l):
    if l[0] <= l[1] <= l[2] or l[2] <= l[1] <= l[0]:
        return l[1]
    elif l[1] <= l[0] <= l[2] or l[2] <= l[0] <= l[1]:
        return l[0]
    else:
        return l[2]

if __name__ == "__main__":
    l = range(500)
    rl = l[::-1]
    randoml = random.sample(range(1000000), 1000000)
    # print "quickshort l"
    # quicksort_wrapper(l)
    # print "random quickshort l"
    # random_quicksort_wrapper(l)
    # print "median quickshort l"
    # median_quicksort_wrapper(l)
    # print "quickshort rl"
    # quicksort_wrapper(rl)
    # print "random quickshort rl"
    # random_quicksort_wrapper(rl)
    # print "median quickshort rl"
    # median_quicksort_wrapper(rl)
    print "quickshort randoml"
    quicksort_wrapper(randoml)
    print "random quickshort randoml"
    random_quicksort_wrapper(randoml)
    print "median quickshort randoml"
    median_quicksort_wrapper(randoml)


