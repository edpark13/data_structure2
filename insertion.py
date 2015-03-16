#! /usr/bin/env python


def insertion_sort(lis):
    for x in xrange(len(lis)):
        i = x
        while i > 0 and lis[i-1] > lis[i]:
            lis[i], lis[i-1] = lis[i-1], lis[i]
            i -= 1
    return lis


if __name__ == '__main__':
    l = [4, 3, 6, 8, 1 ,5]
    print l
    insertion_sort(l)
    print l
