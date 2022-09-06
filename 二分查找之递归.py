def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            return binarySearch(alist[midpoint:], item)
        else:
            return binarySearch(alist[:midpoint], item)


alist = [1, 2, 3, 4, 5, 66, 88, 95]
print(binarySearch(alist, 66))
print(binarySearch(alist, 12))

'''
二分查找时间复杂度为O(log n)
'''
