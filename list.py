def makelist(num):
    l = []
    for i in xrange(num):
        l.append(i)
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


if __name__ == "__main__":
    print makelist(16)
