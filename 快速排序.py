def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

    return alist


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    splitValue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= splitValue:
            leftmark = leftmark + 1

        while rightmark >= leftmark and alist[rightmark] >= splitValue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


alist = [18, 56, 32, 4, 88, 23, 66, 12, 32, 7, 31]
print(quickSort(alist))
'''
时间复杂度为O(nlog n)
根据中值选取相关，极端情况下为O(n^2)，加上递归开销，不如冒泡
'''
