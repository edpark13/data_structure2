def makelist(num):
    even = makeeven(num)
    odd = makeodd(num)
    even.extend(odd)
    return even


def makeeven(num):
    l = []
    for i in xrange(num):
        if i % 2 == 0:
            l.append(i)
    return l


def makeodd(num):
    l = []
    for i in xrange(num):
        if i % 2 == 1:
            l.append(i)
    return l

if __name__ == "__main__":
    makelist(100)
