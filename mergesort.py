def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        left = l[:len(l)/2]
        right = l[len(l)/2:]

        left = merge_sort(left)
        right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

if __name__ == "__main__":
    l = [10, 2, 5, 1, 2, 4, 8, 6]
    print 'before sort' + str(l)
    l = merge_sort(l)
    print 'after sort' + str(l)
