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
    # print 'l = ' + str(l)
    r = []
    while len(l) > 2:
        a = l.pop(2)
        b = l.pop(0)
        # print 'a = ' + str(a)
        # print 'b = ' + str(b)
        r.append(a)
        r.append(b)
    if len(l) % 2 == 0:
        r.append(l[1])
    r.append(l[0])
    return r


def makeodd(num):
    l = []
    for i in xrange(num):
        if i % 2 == 1:
            l.append(i)
    r = []
    while len(l) > 2:
        a = l.pop(2)
        b = l.pop(0)
        # print 'a = ' + str(a)
        # print 'b = ' + str(b)
        r.append(a)
        r.append(b)
    if len(l) % 2 == 0:
        r.append(l[1])
    r.append(l[0])
    return r

if __name__ == "__main__":
    print makelist(16)
