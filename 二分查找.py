def binarySearch(alist, item):
    start = 0
    end = len(alist) - 1
    found = False
    while start <= end and not found:
        midpoint = (start + end) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] > item:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return found


alist = [1, 2, 3, 4, 5, 66, 88, 95]
print(binarySearch(alist, 66))

