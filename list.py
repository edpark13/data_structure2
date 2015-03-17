def makelist(l):
    left = l[:len(l)/2]
    right = l[len(l)/2:]
    final_list = []
    while left and right:
        final_list.append(right.pop(0))
        final_list.append(left.pop(0))
    while left:
        final_list.append(left.pop(0))
    while right:
        final_list.append(right.pop(0))
    return final_list

def makeworstlist(num):
    l = []
    for i in xrange(num):
        l.append(i)
    even = makeeven(l)
    odd = makeodd(l)
    even.extend(odd)
    return even

def makeeven(l):
    even = []
    for i in xrange(len(l)):
        if l[i] % 2 == 0:
            even.append(i)
    return makelist(even)

def makeodd(l):
    odd = []
    for i in xrange(len(l)):
        if l[i] % 2 == 1:
            odd.append(i)
    return makelist(odd)


if __name__ == "__main__":
    print makeworstlist(10)
